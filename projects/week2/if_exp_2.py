def str_diff(str1, str2):
    if type(str1) != str or type(str2) != str:
        return 0
    elif str1 == str2:
        return 1
    elif len(str1) > len(str2):
        return 2
    elif str2 == 'learn':
        return 3

print(str_diff(1, 'aa'))
# 0
print(str_diff('aa', 2))
# 0
print(str_diff(1, 2))
# 0
print(str_diff('aa', 'aa'))
# 1
print(str_diff('aab', 'aa'))
# 2
print(str_diff('aab', 'learn'))
# 3
print(str_diff('aab', 'aabbb'))
# None


