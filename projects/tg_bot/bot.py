import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(format='%(asctime)s - %(message)s', filename='bot.log', level=logging.INFO)

PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

vowels = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я']

def greet_user(update, context):
    print('Сучара нажал на старт!')
    user_first_name = update.message.chat.first_name
    update.message.reply_text(f'Здорова, Сучара({user_first_name})!')

def echo_ans(update, context):
    text = update.message.text
    print(text)
    ans_text = ''
    for i in (text):
        ans_text = ans_text + i
        if i in vowels:
            ans_text = ans_text + 'пу'
    print(ans_text)
    update.message.reply_text(ans_text)  

def main():
    mybot = Updater(settings.API_KEY, 
                    use_context=True, 
                    request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, echo_ans))
    
    logging.info('Sychara is starting')

    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
