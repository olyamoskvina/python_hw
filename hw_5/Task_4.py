# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Например, 

# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW - 12W1B12W3B24W1B14W

my_str = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
s = ''
i = 0
while i < len(my_str):
    count = 1
    while i + 1 < len(my_str) and my_str[i] == my_str[i + 1]:
        count = count + 1
        i = i + 1
    s += str(count) + my_str[i]
    i += 1
print(s)