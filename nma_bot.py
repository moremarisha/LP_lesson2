# coding = UTF-8
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import planet
import datetime
import lp2_while


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='nma_bot.log'
                    )

# Настройки прокси
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def run_planet_constellation(bot, update):
    #planet_name = input('enter a planet name: ')
    update.message.reply_text('enter a planet name')
    planet_name = update.message.text
    today = datetime.date.today()
    (planet_name_eng, err) = planet.get_eng_planet_name(planet_name)
    if err == '':
        cons_name = planet.get_constellation(planet_name_eng, today)
        update.message.reply_text('now the planet {planet} in the constellation {cons}'.format(planet=planet_name_eng,
                                                                                               cons=cons_name))
    else:
        update.message.reply_text(err)


def main():
    mybot = Updater('514216029:AAGrjbrD5N7NvsWwcWGcTfEcelwF_xWy71s', request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    #dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    #dp.add_handler(CommandHandler("lets_talk", lp2_while.ask_user()))
    dp.add_handler(CommandHandler("planet", run_planet_constellation))

    mybot.start_polling() #запрос к телеге
    mybot.idle()


#if __name__ == '__main__':
main()