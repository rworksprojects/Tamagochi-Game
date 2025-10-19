health = 5
coins = 5
def damage():
    global health
    health -= 1
def heal():
    global health
    health += 1
def money():
    global coins
    coins += 1
def minus():
    global coins
    coins -= 1
def show():
    print(f'Здоровье: {health}')
    print(f'Монеты: {coins}')
def game():
    try:
        while True:
            d = input("1 - отдохнуть, 2 - искать монеты: ")
            if d == '1':
                heal()
                minus()
                show()
            elif d == '2':
                money()
                damage()
                show()
            else:
                print("Я не понимаю")
            if coins <= 0 or health <= 0:
                print("Ты проиграл!")
                quit()
    except:
        pass
game()