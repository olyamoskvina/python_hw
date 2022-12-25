# 3 Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

num = int(input('Enter number of elements in list: '))
my_list = []
for i in range(num):
    my_list.append(round(random.uniform(0, 10), 2))
# print(my_list)

my_list1 = []
for i in my_list:
    if i % 1 != 0:
        my_list1.append(round(i % 1, 2))
# print(my_list1)

print(max(my_list1) - min(my_list1))
