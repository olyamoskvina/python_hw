# 5 Реализуйте алгоритм перемешивания списка.

import random 

num = int(input('введите число: '))
my_list = []
for i in range (num):
    my_list.append(random.randint(-num, num))
print(my_list)

random.shuffle(my_list)
print(my_list)