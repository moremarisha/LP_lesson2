# coding = UTF-8
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import datetime
import re

import lp2_while
import planet
import bot_constants
import mycalc


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='nma_bot.log'
                    )

# Настройки прокси
PROXY = bot_constants.bot_proxy


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    if user_text[-1] == '=':
        print(user_text[-1])
        mycalc.run_calc(user_text)
    else:
        update.message.reply_text(user_text)


def run_planet_constellation(bot, update):
    #planet_name = input('enter a planet name: ')
    planet_from_user = update.message.text
    planet_name = planet_from_user.split('/planet ')[1]
    print('planet_name: ', planet_name)
    today = datetime.date.today()
    (planet_name_eng, err) = planet.get_eng_planet_name(planet_name)
    print('planet_name_eng: ', planet_name_eng)
    print('err: ', err)
    if not err:
        print('err is null')
        cons_name = planet.get_constellation(planet_name_eng, today)
        print('cons_name: ', cons_name)
        update.message.reply_text(
            'now the planet {planet} in the constellation {cons}'.format(
                planet=planet_name_eng,
                cons=cons_name))
    else:
        update.message.reply_text(err)


def run_wordcount(bot, update):
    print('start wordcount')
    str_from_user = update.message.text
    if len(str_from_user) > 11:
        print(str_from_user.split('/wordcount '))
        str_analyse = str_from_user.split('/wordcount ')[1]
    else:
        res = 'you entered an empty string!'
        print(res)
        update.message.reply_text(res)
        return

    str_analyse = str_analyse.strip()
    first_simbol = str_analyse[0]
    last_simbol = str_analyse[-1]
    print(first_simbol, last_simbol)
    if first_simbol != '"' and last_simbol != '"':
        res = 'please enter quoted strings'
        print(res)
        update.message.reply_text(res)
        return
    str_analyse = str_analyse.strip('"')
    str_analyse = str_analyse.strip()
    str_analyse = re.sub(' +', ',', str_analyse)
    str_analyse_list = str_analyse.split(' ')
    word_count = len(str_analyse_list)
    res = 'number of words: ' + str(word_count)
    print(res)
    update.message.reply_text(res)

def main():
    mybot = Updater(bot_constants.bot_key, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    #dp.add_handler(CommandHandler("lets_talk", lp2_while.ask_user()))
    dp.add_handler(CommandHandler("planet", run_planet_constellation))
    dp.add_handler(CommandHandler("wordcount", run_wordcount))

    mybot.start_polling() #запрос к телеге
    mybot.idle()


# if __name__ == '__main__':
main()
