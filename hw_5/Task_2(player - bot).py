from random import randint as rand

all_candies = 200       # всего конфет
take_candy = 0           # игрок берет конфеты
player_candy = 0         # сколько конфет у игрока
bot_candy = 0            # сколько конфет у бота

def start_game():
    print(f' На столе лежит {all_candies} конфета.\n Играют два игрока делая ход друг после друга.\n За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. \n Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?')

start_game()

def player_move():
    global all_candies
    global take_candy
    global player_candy
    print(f'Сейчас ваш ход. На столе {all_candies} конфет')
    take_candy = int(input('Сколько конфет вы берете?: '))
    while take_candy > 28 or take_candy < 0 or take_candy > all_candies:
        take_candy = int(input('Вы взяли много конфет. Возьмите снова: '))
    all_candies -= take_candy
    player_candy += take_candy
    if all_candies > 0:
        bot_move()
    else:
        print('Вы выиграли!')
        



def bot_move():
    global all_candies
    global take_candy
    global bot_candy
    import random
    take_candy = random.randint(1, 28)
    all_candies -= take_candy
    bot_candy += take_candy
    print(f'Бот взял {take_candy} конфет. Осталось {all_candies} конфет')
    if all_candies > 0:
        player_move()
    else:
        bot_candy = all_candies
        print('Бот выиграл!')



# Жеребьевка

def first_move():
    random_num = rand(1, 2)
    if random_num == 1:
        player_move()
    else :
        bot_move()


first_move()
player_move()
bot_move() 