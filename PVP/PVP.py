player_one = 'Player_one'
player_two = 'Player_two'
game_field = ([0,1,2],[3,4,5],[6,7,8])
print("выберите ячейку")
def game():
    while True:
        while True:
            print_string()
            print('Player_1, Сделайте свой ход\nВыберите строку([0,2]')
            line = int(input())
            if valid(line) !='OK':
                print('_____ОШИБКА ВВЕДЕННЫХ ДАННЫХ_____')
                continue
            print('Выберите ячейку')
            column = int(input())
            if valid(column) !='OK':
                print('_____ОШИБКА ВВЕДЕННЫХ ДАННЫХ_____')
                continue
            if game_field[line][column] == 'X' or game_field[line][column]=='O':
                print('_____ЗАНЯТО_____')
                continue
            game_field[line][column] = "X"
            print_string()
            print('_____________________')
            if check() == 'win':
                print('GAME OVER')
                return
            break
        while True:
            print_string()
            print('Player_2, Сделайте свой ход\nВыберите строку([0,2]')
            line = int(input())
            if valid(line) !='OK':
                print('_____ОШИБКА ВВЕДЕННЫХ ДАННЫХ_____')
                continue
            print('Выберите ячейку')
            column = int(input())
            if valid(column) !='OK':
                print('_____ОШИБКА ВВЕДЕННЫХ ДАННЫХ_____')
                continue
            if game_field[line][column] == 'X' or game_field[line][column]=='O':
                print('_____ЗАНЯТО_____')
                continue
            game_field[line][column] = "O"
            print_string()
            print('_____________________')
            if check() == 'win':
                print('GAME OVER')  
                return          
            break
def print_string():
    return print(f'{game_field[0][0]}|{game_field[0][1]}|{game_field[0][2]}\n-----\n{game_field[1][0]}|{game_field[1][1]}|{game_field[1][2]}\n-----\n{game_field[2][0]}|{game_field[2][1]}|{game_field[2][2]}')
def valid(number):
    if number < 0 or number > 2:
        return "error"
    else: 
        return 'OK'
def check():
    #вертикаль
    if game_field[0][0] == game_field[0][1] == game_field[0][2]:
        return 'win'
    if game_field[1][0] == game_field[1][1] == game_field[1][2]:
        return 'win'
    if game_field[2][0] == game_field[2][1] == game_field[2][2]:
        return 'win'
    #диагональ
    if game_field[0][0] == game_field[1][1] == game_field[2][2]:
        return 'win'
    if game_field[2][0] == game_field[1][1] == game_field[0][2]:
        return 'win'
game()
