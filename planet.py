# coding = UTF-8
import ephem
import datetime
import logging

def get_eng_planet_name(planet_name):
    err = ''
    planet_name_eng = ''
    if planet_name.lower() == 'меркурий' or planet_name.lower()=='mercury':
        planet_name_eng = 'Mercury'
    elif planet_name.lower() == 'венера' or planet_name.lower()=='venus':
        planet_name_eng = 'Venus'
    elif planet_name.lower() == 'земля' or planet_name.lower()=='earth':
        planet_name_eng = 'Earth'
    elif planet_name.lower() == 'марс' or planet_name.lower()=='mars':
        planet_name_eng = 'Mars'
    elif planet_name.lower() == 'юпитер' or planet_name.lower()=='jupiter':
        planet_name_eng = 'Jupiter'
    elif planet_name.lower() == 'сатурн' or planet_name.lower()=='saturn':
        planet_name_eng = 'Saturn'
    elif planet_name.lower() == 'уран' or planet_name.lower()=='uranus':
        planet_name_eng = 'Uranus'
    elif planet_name.lower() == 'нептун' or planet_name.lower()=='neptune':
        planet_name_eng = 'Neptune'
    else:
        err = 'There is no such planet'

    return planet_name_eng, err


def get_constellation(planet_name, date):
    #print('get_constellation: ', planet_name)
    if planet_name == 'Mercury':
        planet = ephem.Mercury(date)
    elif planet_name == 'Venus':
        planet = ephem.Venus(date)
    elif planet_name == 'Earth':
        planet = ephem.Earth(date)
    elif planet_name == 'Mars':
        planet = ephem.Mars(date)
    elif planet_name == 'Jupiter':
        planet = ephem.Jupiter(date)
    elif planet_name == 'Saturn':
        planet = ephem.Saturn(date)
    elif planet_name == 'Uranus':
        planet = ephem.Uranus(date)
    elif planet_name == 'Neptune':
        planet = ephem.Neptune(date)
    #print(planet)
    cons_name = ephem.constellation(planet)
    print('now the planet {planet} in the constellation {cons}'.format(planet=planet_name_eng,
                                                                       cons=cons_name))
    #return (cons_name)


if __name__ == '__main__':
    planet_name = input('enter a planet name: ')
    today = datetime.date.today()
    (planet_name_eng, err) = get_eng_planet_name(planet_name)
    if err == '':
        print('planet_name_eng in main: ', planet_name_eng)
        get_constellation(planet_name_eng, today)
    else:
        print (err)
