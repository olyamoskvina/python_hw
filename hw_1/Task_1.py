# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
#     - 6 -> да
#     - 7 -> да
#     - 1 -> нет

day_number = int(input('Enter number from 1 to 7: '))
if 1 <= day_number <= 5:
    print('No')
elif day_number == 6 or day_number == 7:
    print('Yes')
else:
    print('You entered incorrect number. Try again')