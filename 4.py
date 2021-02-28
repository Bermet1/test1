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

