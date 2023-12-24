#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Объявите функцию, которая принимает строку на кириллице и преобразовывает ее в латиницу, используя следующий
# словарь для замены русских букв на соответствующее латинское написание. Функция должна возвращать
# преобразованную строку. Замены делать без учета регистра (исходную строку перевести в нижний регистр – малые
# буквы). Определите декоратор с параметром chars и начальным значением "!?", который данные символы преобразует в # символ "-" и, кроме того, все подряд идущие дефисы (например, "--" или "---" ) приводит к одному дефису.
# Полученный результат должен возвращаться в виде строки. Примените декоратор со значением chars="?!:;,. " к 
# функции и вызовите декорированную функцию. Результат отобразите на экране.


def pink(func):

    def pnk(text, chars=" !?"):

        print(text)

        h = ''.join(map(lambda x: x if x not in chars else '-', func(text)))
        print(h)
        while '--' in h:
            h = h.replace('--', '-')
        print(h)
        return h

    return pnk
@pink
def wrapper(text):
    p = text.lower()
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e',
         'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l',
         'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
         'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
         'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu',
         'я': 'ya'}
    return p.translate({ord(key): t[key] for key in t})


if __name__ == "__main__":
    s = 'Я щ --- ! ? - ?У лукоморья дуб зелёный; Златая цепь на дубе том: \
    И днём и ночью кот учёный\
     Всё ходит по цепи кругом;'

    x = wrapper(s)
