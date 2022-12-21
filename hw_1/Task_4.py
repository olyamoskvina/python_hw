# 4 Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def get_coordinates (quarter):
    if quarter == 1:
        print('x[0;+∞] y[0;+∞]')
    elif quarter == 2:
        print('x[0;-∞] y[0;+∞]')
    elif quarter == 3:
        print('x[0;-∞] y[0;-∞]')
    elif quarter == 4:
        print('x[0;+∞] y[0;-∞]')
    else:
        print('You entered incorrect quarter. Try again.')
    return

num_quarter = int(input('Enter quarter number: '))    
get_coordinates(num_quarter)  

exit()

number = input('введите четверть')
if (number == '1'):
    print("(X >0 и Y > 0)")
elif (number == '2'):
    print("(X >0 а Y < 0)")
elif (number == '3'):
    print("(X < 0 и Y < 0)")
elif (number == '4'):
    print("(X > 0 и Y < 0)")
else:print("Неправильный ввод")