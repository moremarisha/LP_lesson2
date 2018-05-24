import sys
import re
import logging


def run_calc(calc_str):
    res = 0
    err = ''
    print('run_calc: ', calc_str)
    calc_str_clean = calc_str.replace(' ', '')
    add_parts = calc_str_clean.split('+')
    for i in range(len(add_parts)):
        print('add_part: ', add_parts[1])
        if '-' in add_parts[i]:
            subtract_list = add_parts[i].split('-')
            for j in range(len(subtract_list)):
                subtract_list[j] = precalculate(subtract_list[j])
            print(subtract_list)
            add_parts[i] = subtract_list[0] - sum(subtract_list[1:])
            print(add_parts[i])

    print(add_parts)
    res = sum(map(float, add_parts))
    return res, err


def precalculate(str):
    res_str = float(str)
    return res_str

if __name__ == '__main__':
    exit_flag = '1'
    while exit_flag == '1':
        calc_str = input('что посчитать?')
        if calc_str[-1] != '=':
            print('в конце должнен быть знак "="!')
        else:
            calc_str = '10+2  8*2 +35/5 - 1   +14='
            calc_str = '13+14-1-7  + 9='
            (res, err) = run_calc(calc_str[:-1])
        exit_flag = err
    if not err:
        print('Результат: ', str(res))
    else:
        print('Error: ', err)
