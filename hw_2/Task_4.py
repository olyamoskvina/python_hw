# 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

import random 

num = int(input('введите число: '))
my_list = []
for i in range (num):
    my_list.append(random.randint(-num, num))
print(my_list)


path = 'file.txt'
data = open(path, 'w')
data.write('1\n')
data.write('4\n')
data.close()
# print(data)

 
data = open(path,'r')
multiply = 1
for line in data :
    multiply *= my_list[int(line)]
print(multiply)