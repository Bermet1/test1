import random 
num = random.randint(1, 20)

tries = 0 
guess = 0

while num != guess and tries < 6:
    print("Угадай число от 1 до 20")
    guess = int(input())
    tries += 1
    if tries == 5:
        print("Вы проиграли! Игра завершилась")
    elif guess < num:
        print("слишком мало")
    elif guess > num:
        print("Слишком много")
    elif guess == num:
        print("Класс! Вы угадали!")
        break
    