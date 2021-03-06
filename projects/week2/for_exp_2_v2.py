import math

def calc_square_len(input_string):
    input_string_len = len(input_string)
    square_len = math.sqrt(input_string_len)
    if int(square_len) ** 2 != input_string_len:
        square_len = int(square_len)
    else:
        square_len = int(square_len) - 1
    return square_len         

def cant_move_left(x_min, x_max, y_min, y_max, x_direction, y_direction, x_cur, y_cur):
    y_min +=1
    x_direction = 0
    y_direction = 1
    return x_min, x_max, y_min, y_max, x_direction, y_direction, x_cur, y_cur

def cant_move_right(x_min, x_max, y_min, y_max, x_direction, y_direction, x_cur, y_cur):
    y_max -= 1
    x_direction = 0
    y_direction = -1
    return x_min, x_max, y_min, y_max, x_direction, y_direction, x_cur, y_cur

def cant_move_up(x_min, x_max, y_min, y_max, x_direction, y_direction, x_cur, y_cur):
    x_max -= 1
    x_direction = -1
    y_direction = 0
    return x_min, x_max, y_min, y_max, x_direction, y_direction, x_cur, y_cur

def cant_move_down(x_min, x_max, y_min, y_max, x_direction, y_direction, x_cur, y_cur):
    x_min += 1
    x_direction = 1
    y_direction = 0
    return x_min, x_max, y_min, y_max, x_direction, y_direction, x_cur, y_cur        

def change_direction(x_min, x_max, y_min, y_max, x_direction, y_direction, x_cur, y_cur):
    cant_go = True
    if x_cur == x_min and x_direction == -1:
        where_cant_go = cant_move_left
    elif x_cur == x_max and x_direction == 1:
        where_cant_go = cant_move_right
    elif y_cur == y_min and y_direction == -1:
        where_cant_go = cant_move_up
    elif y_cur == y_max and y_direction == 1:
        where_cant_go = cant_move_down
    else:
        cant_go = False
    if cant_go:
        x_min, x_max, y_min, y_max, x_direction, y_direction, x_cur, y_cur = where_cant_go(x_min, x_max, y_min, y_max, x_direction, y_direction, x_cur, y_cur)    
    return x_min, x_max, y_min, y_max, x_direction, y_direction, x_cur, y_cur

def create_print_order_square(input_string, x_min, x_max, y_min, y_max, x_direction, y_direction, x_cur, y_cur):
    print_order_square = {}
    input_string_len = len(input_string)
    for cur_letter in range(input_string_len):
        print_order_square[(x_cur, y_cur)] = cur_letter
        x_cur += x_direction
        y_cur += y_direction
        x_min, x_max, y_min, y_max, x_direction, y_direction, x_cur, y_cur = change_direction(x_min, x_max, y_min, y_max, x_direction, y_direction, x_cur, y_cur)
    return print_order_square

def create_print_order_square_v2(input_string, square_len, x_min, x_max, y_min, y_max, x_direction, y_direction, x_cur, y_cur):
    print_order_square = {(x, y): None for x in range(square_len) for y in range(square_len)}
    input_string_len = len(input_string)
    letter_order_number = 0
    while letter_order_number < input_string_len:
        print_order_square[(x_cur, y_cur)] = letter_order_number
        letter_order_number += 1
        x_cur += x_direction
        y_cur += y_direction
        x_min, x_max, y_min, y_max, x_direction, y_direction, x_cur, y_cur = change_direction(x_min, x_max, y_min, y_max, x_direction, y_direction, x_cur, y_cur)
    return print_order_square

def print_input_string_with_print_order_square(input_string, print_order_square, square_len):
    for y_square in range(0, square_len + 1):
        for x_square in range(0, square_len + 1):
            print_order_square_key = (x_square, y_square)
            print_string_number = print_order_square.get(print_order_square_key)
            if print_string_number is None:
                print(' ', end='')
            else:
                print(input_string[print_string_number], end='')
        print()


def main():
    input_string = input('Введите строку, распечатаем её красиво: ')

    square_len = calc_square_len(input_string)

    x_min, x_max, y_min, y_max, x_direction, y_direction, x_cur, y_cur = 0, square_len, 0, square_len, -1, 0, square_len, 0

    print_order_square = dict(create_print_order_square_v2(input_string, square_len, x_min, x_max, y_min, y_max, x_direction, y_direction, x_cur, y_cur))
    
    print_input_string_with_print_order_square(input_string, print_order_square, square_len)     

if __name__ == "__main__":
    main()




