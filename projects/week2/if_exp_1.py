def what_to_do(age):
    what_doing = ''
    if age < 0:
        return 'введен некорректный возраст (<0)'
    elif 0 <= age < 6:
        what_doing = 'в детский сад'
    elif 6 <= age <= 18:
        what_doing = 'в школу'
    elif 19 <= age <= 24:
        what_doing = 'в университет'
    elif 25 <= age <= 65:
        what_doing = 'на работу'
    else:
        what_doing = 'на пенсию'
    return f'Пора {what_doing}!'


age = input('Введите ваш возраст: ')
age = int(age)

where_i_going = what_to_do(age)

print (where_i_going)

