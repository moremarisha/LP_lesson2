import sys
import re


def run_calc(calc_str):
    res = 0
    err = ''
    calc_str = calc_str.strip('=')
    try:
        res = eval(calc_str)
        return res, err
    except:
        err = 'введите корректную строку!'
        return res, err
    




if __name__ == '__main__':
    calc_str = input('что посчитать?')

    if calc_str[-1] != '=':
        print('в конце должнен быть знак "="!')
        sys.exit()

    (res, err) = run_calc(calc_str)
    if err == '':
        print('Результат: ', str(res))
    else:
        print('Error: ', err)
