# 4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

binary_num = ""
num = int(input("Enter number:\n"))
while num != 0:
    binary_num = str(num%2) + binary_num
    num //=2
print(binary_num)