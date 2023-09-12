import random


def choice(complexity,game_field):
    if complexity == 1:
        data = easy(game_field)
        return data
    elif complexity == 2:
        data = medium(game_field)
        return data
    

def easy(game_field):
    while True:
        line = random.randrange(3)
        column = random.randrange(3)
        if game_field[line][column] == 'X' or game_field[line][column]=='O':
            continue
        else: 
            data = (line,column)
            return data
    return
def medium(game_field):
    for i in range(3):

        number = 0
        bnumber = 0 
        n = 0
        bn = 0
        index = 0
        cnumber = 0
        if type(game_field[0][0]) is int  or type(game_field[0][1]) is int or type(game_field[0][2]) is int:
            if type(game_field[1][0]) is int or type(game_field[1][1]) is int  or type(game_field[1][2]) is int:
                if type(game_field[2][0]) is int or type(game_field[2][1]) is int or type(game_field[2][2]) is int :
                    for k in range(3):
                        bnumber+=1
                        if game_field[i][k] == 'X':
                            number+=1
                        elif game_field[i][k] != 'X':
                            index = k
                        if number == 2 and bnumber == 3:
                                data = (i,index)
                                print('гориз')
                                return data 
        if type(game_field[0][0]) is int or type(game_field[1][0]) is int or type(game_field[2][0]) is int:
            if type(game_field[0][0]) is int or type(game_field[1][1]) is int  or type(game_field[2][1]) is int:
                if type(game_field[0][2]) is int or type(game_field[1][2]) is int or type(game_field[2][2]) in int:
                    for p in range(3):
                        cnumber = 0
                        number = 0
                        for w in range(3):
                            cnumber+=1
                            if game_field[w][p] == 'X':
                                number+=1
                            elif game_field[w][p] != 'X':
                                index = p
                            if number == 2 and cnumber == 3:
                                    data = (w,index)
                                    print('вертик')
                                    return data 

        for j in range(3):
            bn +=1
            free = 0
            if game_field[i][j] == 'O':
                n+=1
            elif type(game_field[i][j]) is int:
                free = j
            if bn == 3 and n == 2:
                data = (i,free)
                return data
    for q in range(3):
        print(game_field)
        if type(game_field[q][0]) is int   and type(game_field[q][1])  is int and type(game_field[q][2]) is int :
            data = (q,random.randrange(3))
            print("one")
            return data
        elif type(game_field[0][q]) is int  and type(game_field[1][q]) is int  and type(game_field[2][q]) is int :
            data = (q,random.randrange(3))
            print("two")
            return data
        elif type(game_field[0][0]) is int and type(game_field[1][1]) is int and type(game_field[2][2]) is int :
            data = (2,random.randrange(3))
            print("tree")
            return data
