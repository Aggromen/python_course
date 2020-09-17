import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
from googletrans import Translator
# pip install googletrans (https://pypi.org/project/googletrans/)
import ephem
import pylev
# pip install pylev (https://pypi.org/project/pylev/)


logging.basicConfig(format='%(asctime)s - %(message)s', filename='bot.log', level=logging.INFO)

PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

vowels = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я']

planet_list = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

def greet_user(update, context):
    print('Сударь нажал на старт!')
    user_first_name = update.message.chat.first_name
    update.message.reply_text(f'Здорова, Сударь({user_first_name})!')

def echo_ans(update, context):
    text = update.message.text
    print(text)
    ans_text = ''
    for letter in text:
        ans_text = ans_text + letter
        if letter.lower() in vowels:
            ans_text = ans_text + 'пу'
    print(ans_text)
    update.message.reply_text(ans_text)  

def translate_message_to_eng(update, context):
    translator = Translator()
    text = update.message.text
    ans_text = translator.translate(text, src='russian')
    update.message.reply_text(ans_text.text)

def find_constellation(best_planet_choice):
    time_now = ephem.now()
    planet_obj = getattr(ephem, best_planet_choice)
    user_find_planet = planet_obj()                                
    user_find_planet.compute(time_now)
    _, full_name = ephem.constellation(user_find_planet)
    return full_name

def planet_constellation(update, context):
    translator = Translator()
    text = update.message.text
    text = text.split()
    min_distance = 1000
    best_planet_choice = ''
    user_planet_in_text = ''
    for cur_word in text:
        for cur_planet in planet_list:
            if pylev.levenshtein(cur_word, cur_planet) < min_distance:
                min_distance = pylev.levenshtein(cur_word, cur_planet)
                best_planet_choice = cur_planet
                user_planet_in_text = cur_word
    full_name = find_constellation(best_planet_choice)
    full_name_ru = translator.translate(full_name,dest='russian', src='en').text
    if user_planet_in_text.upper() != best_planet_choice.upper():
        ans_text = f'Did you mean {best_planet_choice}? \n {full_name} / {full_name_ru}'
    else:
        ans_text = f'{full_name} / {full_name_ru}'
    update.message.reply_text(ans_text)            



def main():
    mybot = Updater(settings.API_KEY, 
                    use_context=True, 
                    request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('translate_to_eng', translate_message_to_eng))
    dp.add_handler(CommandHandler('planet', planet_constellation))
    dp.add_handler(MessageHandler(Filters.text, echo_ans))
    
    logging.info('user is starting')

    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
