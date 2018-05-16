# -*- coding: utf-8 -*-

def age_analyser (age):
    if age < 0:
        res = 'Вы ввели неверный возраст'
    elif age >= 0 and age < 3:
        res = 'Вы совсем крошка'
    elif age >= 3 and age < 7:
        res = 'Вы ходите в детский сад'
    elif age >= 7 and age < 18:
        res = 'Вы учитесь в школе'
    elif age >= 18 and age < 23:
        res = 'Вы учитесь в ВУЗ'
    elif age >=23:
        res = 'Вы работаете на работе:('

    print (res)
    return res


def string_analyser(str1, str2):
    if str1 == str2:
        res = 1
    else:
        if len(str1) > len(str2):
            res = 2
        elif str2 == 'learn':
            res = 3
    print(res)
    return res


age_str = input ('Введите Ваш возраст: ')
age = float (age_str)
res_age = age_analyser(age)

print('------------------')

str1 = input('Введите строку: ')
str2 = input('Введите еще одну строку: ')
res_str = string_analyser(str1, str2)