from random import randint as rand

all_candies = 200       # всего конфет
take_candy = 0           # игрок берет конфеты
player1_candy = 0         # сколько конфет у игрока
player2_candy = 0            # сколько конфет у бота


def start_game():
    print(' На столе лежит 2021 конфета.\n Играют два игрока делая ход друг после друга.\n За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. \n Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?')

start_game()

def player1_move():
    global all_candies
    global take_candy
    global player1_candy
    print(f'Сейчас ваш ход. На столе {all_candies} конфет')
    take_candy = int(input('Сколько конфет вы берете?: '))
    while take_candy > 28 or take_candy < 0 or take_candy > all_candies:
        take_candy = int(input('Вы взяли много конфет. Возьмите снова: '))
    all_candies -= take_candy
    player1_candy += take_candy
    if all_candies > 0:
        player2_move()
    else:
        print('Игрок -1 выиграл!')
    return
       


def player2_move():
    global all_candies
    global take_candy
    global player2_candy
    print(f'Сейчас ход Игрока -2 . На столе {all_candies} конфет')
    take_candy = int(input('Сколько конфет вы берете?: '))
    while take_candy > 28 or take_candy < 0 or take_candy > all_candies:
        take_candy = int(input('Вы взяли много конфет. Возьмите снова: '))
    all_candies -= take_candy
    player2_candy += take_candy
    if all_candies > 0:
        player1_move()
    else:
        print('Игрок - 2 выиграл!')
    return
   

# Жеребьевка
def first_move():
    random_num = rand(1, 2)
    if random_num == 1:
        player1_move()
    else :
        player2_move()


first_move()
player1_move()
player2_move() 