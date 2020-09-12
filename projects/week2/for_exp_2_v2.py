import math

def change_direction(x_min, x_max, y_min, y_max, x_direction, y_direction, x_cur, y_cur):
    if x_cur == x_min and x_direction == -1:
        y_min +=1
        x_direction = 0
        y_direction = 1
    elif x_cur == x_max and x_direction == 1:
        y_max -= 1
        x_direction = 0
        y_direction = -1
    elif y_cur == y_min and y_direction == -1:
        x_max -= 1
        x_direction = -1
        y_direction = 0
    elif y_cur == y_max and y_direction == 1:
        x_min += 1
        x_direction = 1
        y_direction = 0
    return x_min, x_max, y_min, y_max, x_direction, y_direction, x_cur, y_cur

input_string = input('Введите строку, распечатаем её красиво: ')

input_string_len = len(input_string)

square_len = math.sqrt(input_string_len)
if int(square_len) ** 2 != input_string_len:
    square_len = int(square_len)
else:
    square_len = int(square_len) - 1

print_order = {}    

x_min, x_max, y_min, y_max, x_direction, y_direction, x_cur, y_cur = 0, square_len, 0, square_len, -1, 0, square_len, 0

for i in range(input_string_len):
    print_order[(x_cur, y_cur)] = i
    x_cur += x_direction
    y_cur += y_direction
    x_min, x_max, y_min, y_max, x_direction, y_direction, x_cur, y_cur = change_direction(x_min, x_max, y_min, y_max, x_direction, y_direction, x_cur, y_cur)

# for i in print_order:
#     print(i, end=' ')
#     print (print_order[i])

# print(input_string_len)
# print(square_len)

for i in range(square_len + 1):
    for j in range(square_len + 1):
        print_order_key = (j, i)
        if print_order_key in print_order:
            print_string_number = print_order[print_order_key]
            print(input_string[print_string_number], end=' ')
        else:
            print(' ', end=' ')
    print()

