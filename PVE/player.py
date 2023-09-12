def input_data():
    print("Введите имя")
    name = str(input())
    while True:
        print("Выбери уровень сложности\nЛегкий-1\nСредний-2\nВысокий-3")
        complexity = int(input())
        if complexity > 3 or complexity < 0:
            continue
        else:
            break
    data = [name,complexity]
    return data
