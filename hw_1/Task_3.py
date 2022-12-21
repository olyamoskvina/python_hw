# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


def get_coordinates(x, y):

    if x > 0 and y > 0:
        print('Quarter 1')
    elif x < 0 and y > 0:
        print('Quarter 2')
    elif x < 0 and y < 0:
        print('Quarter 3')
    elif x > 0 and y < 0:
        print('Quarter 4')
    return


coord_x = int(input('Enter coordinate for X: '))
coord_y = int(input('Enter coordinate for Y: '))


if coord_x == 0 and (coord_y > 0 or coord_y < 0):
    print('Point is on Y axis')
elif coord_y == 0 and (coord_x > 0 or coord_x < 0):
    print('Point is on X axis')
else:
    print('Entered coordinates do not match the task condition. Try again.')

get_coordinates(coord_x, coord_y)