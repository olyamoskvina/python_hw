# 2 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

num = int(input('Enter number: '))
my_list = []
for i in range(num):
    my_list.append(random.randint(-num, num))
print(my_list)

new_list = []
for i in range(int(len(my_list)//2 + len(my_list) % 2)):
    new_list.append(my_list[i] * my_list[-(i+1)])
print(new_list)
