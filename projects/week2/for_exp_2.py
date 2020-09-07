space = ' '
space_num = -1
space_num_shift = 1
space_period = 5
input_string = input('Введите строку, распечатаем её красиво: ')
for i in input_string:
    if space_num == space_period:
        space_num_shift = -1
    elif space_num == 0: 
        space_num_shift = 1
    space_num += space_num_shift
    print_str = space * space_num + i
    print(print_str)

# Ну, попробуй, распечатай!
# Н
#  у
#   ,

#     п
#      о
#     п
#    р
#   о
#  б
# у
#  й
#   ,

#     р
#      а
#     с
#    п
#   е
#  ч
# а
#  т
#   а
#    й

