import re
name_list = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша", "Валера"]


def find_person(name_list, name):
    i=0
    res = 0
    while i < len(name_list):
        if name_list[i] == name:
            print(name_list.pop(i) + ' нашелся!')
            res = 1
        i=i+1
    if res != 1:
        print('Нет таких')


def asc_user():
    ans = ''
    while ans != 'Хорошо':
        ans = input('Как дела? ')

    while ans != 'Пока!':
        ans = input('Скажите что-нибудь: ')
        my_ans = get_answer(ans)[0]
        print(my_ans)


def get_answer(question):
    answers = {'привет': ['И тебе привет!', 0],
               'как дела': ['Норм', 0],
               'пока': ['Пока, пока!', 1],
               'здравствуйте': ['Добрый день!', 0],
               'что делаешь': ['Болтаю с тобой:)', 0],
               'что нового': ['День стал длиннее', 0],
               'до свидания': ['Всего доброго!', 1],
               'не понимаю': ['не понимаю', 0],
               'чтонибудь': ['Самый умный что ли?))', 0],
               'да': ['что "да"??', 0]}

    reg_mask = re.compile('[^а-яА-Я0-9 ]')
    q = reg_mask.sub('', question)
    question_lower = q.lower()
    answer = answers.get(question_lower, ['не понимаю', 0])

    return answer

name = input('Ведите имя для поиска: ')
find_person(name_list, name)

asc_user()
