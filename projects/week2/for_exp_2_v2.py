import math

def change_direction(cur_state):
    x_min = cur_state[0]
    x_max = cur_state[1]
    y_min = cur_state[2]
    y_max = cur_state[3]
    x_direction = cur_state[4]
    y_direction = cur_state[5]
    x_cur = cur_state[6]
    y_cur = cur_state[7]
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
    return [x_min, x_max, y_min, y_max, x_direction, y_direction, x_cur, y_cur]

input_string = input('Введите строку, распечатаем её красиво: ')

input_string_len = len(input_string)

square_len = math.sqrt(input_string_len)
if int(square_len) ** 2 != input_string_len:
    square_len = int(square_len)
else:
    square_len = int(square_len) - 1

print_order = {}    


x_direction, y_direction = -1, 0
x_start, y_start = square_len, 0
x_min, x_max, y_min, y_max = 0, square_len, 0, square_len
x_cur, y_cur = x_start, y_start

cur_state = [x_min, x_max, y_min, y_max, x_direction, y_direction, x_cur, y_cur]

for i in range(input_string_len):
    x_direction = cur_state[4]
    y_direction = cur_state[5]
    x_cur = cur_state[6]
    y_cur = cur_state[7]
    print_order[(x_cur, y_cur)] = i
    x_cur += x_direction
    y_cur += y_direction
    cur_state[6] = x_cur
    cur_state[7] = y_cur  
    cur_state = list(change_direction(cur_state))

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

