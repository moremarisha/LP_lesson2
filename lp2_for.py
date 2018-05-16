school_list = [{'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
               {'school_class': '4b', 'scores': [3, 4, 4, 5, 5]},
               {'school_class': '4v', 'scores': [3, 4, 4, 5, 3]},
               {'school_class': '5a', 'scores': [3, 4, 4, 5, 4, 1, 3, 4, 5]},
               {'school_class': '5b', 'scores': [3, 4, 4, 5, 5, 5, 5, 5]},
               {'school_class': '6a', 'scores': [3, 4, 4, 5, 2, 5,2 ,3]},
               {'school_class': '6b', 'scores': [3, 4, 4, 3]}]

school_res = 0
class_cnt = 0

for sc_class in school_list:
    avg = sum(sc_class['scores'])/ len(sc_class['scores'])
    print('Класс ' + sc_class['school_class'] + ': ' +str(avg))
    school_res = school_res + avg
    class_cnt = class_cnt + 1
school_avg = school_res/class_cnt
print('Результат по школе: ' + str(school_avg))

