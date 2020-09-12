def get_summ(int_1, int_2):
    try:
        int_1 = int(int_1)
        int_2 = int(int_2)
        return int_1 + int_2
    except(ValueError):
        return 'Sorry! No int here'        

if __name__ == "__main__":
    print(get_summ(2, 2))
    print(get_summ(3, "3"))
    print(get_summ("4", "4"))
    print(get_summ("five", 5))
    print(get_summ("six", "шесть"))    