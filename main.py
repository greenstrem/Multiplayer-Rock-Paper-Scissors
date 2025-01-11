import random


print('Приветули')

def comp_choice():
    choices = ["камень", "ножницы", "бумага"]
    return random.choice(choices)

def ask_user():
    x = input(f"Камень, ножницы или бумага?\n").lower()
    while x not in ["камень", "ножницы", "бумага"]:
        print("Выбери из представленного")
        x = input(f"Камень, ножницы или бумага?\n").lower()
    return x

def sanya(pc, user):
    # if pc == user:
    #     print("Ничья")
    rules = {
        "камень":"ножницы",
        "ножницы":"бумага",
        "бумага":"камень"
    }
    if pc == user:
        print("Ничья")
    elif rules[user] == pc:
        print("Ты победил!")
    else:
        print('Ты проиграл!')

def game():
    pc = comp_choice()
    user = ask_user()
    print(f'Компуктер выбрал {pc}\nа ты выбрал {user}')
    sanya(pc = pc, user = user)

game()