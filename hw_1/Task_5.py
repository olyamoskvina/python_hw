# 5 Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

ax = float(input('Enter coordinate AX: '))
ay = float(input('Enter coordinate AY: '))
bx = float(input('Enter coordinate BX: '))
by = float(input('Enter coordinate BY: '))


distance = ((bx - ax) ** 2 + (by - ay) ** 2) ** 0.5
print(f'Distance between {ax, ay} и {bx, by}: {round(distance, 3) }')


exit()

x1, y1 = list(map(int, input('input coords(x1 y1) for first point separated by space - ').split()))
x2, y2 = list(map(int, input('input coords(x2 y2) for first points separated by space - ').split()))

print(round(math.sqrt((x1 - x2)  2 + (y1 - y2)  2), 3))