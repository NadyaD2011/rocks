camnu = 10
otvet = True
reg = 0

# Привет!
print('Это игра "Камешки":')
print(
    """Привет! Я твой соперник в этой игре. Я умён и сообразителен. Не знаю, сможешь ли ты меня победить.
Теперь если ты не испугался, то начнём. Давай договоримся, как будем играть."""
)

# Режим
while not (reg in {2, 3}):
    reg = int(
        input(
            "Выбери для начала сколько можно будет брать максимально камней за один ход - 2 или 3: "
        )
    )

# Правила
print(
    """
Правила игры - просты!
Есть компьютер и игрок. Игрок - это ты. Твоя цель выиграть.
В игре нет ничьи! В ней можно, как проиграть, так и выиграть.
Выигрывает тот кто забирает последний камень.
Ход игры: сначала ты берёшь камень, и потом ходит компьютер и вы ходите по кругу."""
)

# Ход игры
name = input("А как мне тебя называть? ")

print(f"Хорошо, {name}. Начнём!")

while otvet:
    player = 0
    if (camnu > 3 and reg == 3) or (camnu > 2 and reg == 2):
        print("На поле", camnu, "шт. камней.")
        while player < 1 or player > reg:
            player = int(input("Сколько возмёшь камней от 1 до %s? " % reg))
        camnu = camnu - player
        if (camnu > 3 and reg == 3) or (camnu > 2 and reg == 2):
            if reg == 2:
                if camnu % 2 == 1:
                    comp = 2
                else:
                    comp = 1
            else:
                if camnu % 3 == 0:
                    comp = 2
                elif camnu % 3 == 2:
                    comp = 1
                else:
                    comp = 3
            print("Я хожу %s" % comp)
            camnu = camnu - comp
        else:
            print("Я победил! Жаль тебя!")
            otvet = False
    else:
        print("Ты победил!")
        otvet = False

    # Повтор
    if otvet == False:
        povtor = input("Не хочешь повторить? ")
        if povtor.lower() == "да":
            camnu = 10
            otvet = True
        else:
            print("Хорошо. Пока!")

