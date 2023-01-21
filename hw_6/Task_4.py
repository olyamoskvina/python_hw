# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму всех нечептных элементов списка.


import random

num = int(input('введите число: '))
my_list = []
for i in range (num):
    my_list.append(random.randint(-num, num))
print(my_list)


new_list = list(filter(lambda x: (x % 2 != 0), my_list))
print(new_list)
sum = 0
for i in new_list:
    sum = sum + i
print(sum)

