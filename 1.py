#Задание 1
lst = [92, 91, 49, 87, 74, 20, 94, 12, 64, 36, 97, 2, 96, 40, 97, 36, 32, 22, 80, 83, 49, 52, 62, 31,
55, 86, 84, 1, 22, 15, 52, 18, 78, 92, 21, 9, 85, 89, 54, 99, 80, 7, 4, 31, 30, 28, 59, 35, 72, 33]

#способ 1
d = {index: x for index, x in enumerate(lst)}
print(d)

#способ 2
dct = {}

for index, value in enumerate(lst):
    dct[index] = value
print(dct)



#Задание 2
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



#Задание 3
some_string = "Adverts"


a = some_string[2:5]
print(a)



#Задание 4
a = "Aidana"
b = "Adilet"


#Здесь рандомное смешивание двух строк a и b
import random

c = a + b
l = list(c)
random.shuffle(l)
result = ''.join(l)
print(result)


#переводим в список
string_1 = list(a)
string_2 = list(b)
#добавляем в словарь ключ:значение
dic = {string_3: string for string_3, string in zip(string_1, string_2)}
print(dic)
#переводим в строку 
rev = ''.join('{}{}'.format(key, val) for key, val in dic.items())
print(rev)
#резултат AAiddiatne


