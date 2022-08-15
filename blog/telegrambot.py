# myapp/telegrambot.py
# Example code for telegrambot.py module
import logging

from telegram import *
from telegram.ext import *

from .content import allowedContainer, instaContainer

logger = logging.getLogger(__name__)


def echo(update: Update, context: CallbackContext):
    if str(update.message.chat_id) not in allowedContainer.models.keys():
        context.bot.send_message(update.message.chat_id,
                                 text="Ви не зареєстровані (#%s)" % update.message.chat_id)
    else:
        keyBoard = [[InlineKeyboardButton("Показати всіх користувачів", callback_data="showAllUsers")]]
        markUp = InlineKeyboardMarkup(keyBoard)
        context.bot.send_message(update.message.chat_id,
                                 text="Головне меню",
                                 reply_markup=markUp)


def showAllUsers(update: Update, context):
    print("used")
    keyBoard = [[InlineKeyboardButton("Показати всіх користувачів", callback_data="showAllUsers")]]
    markUp = InlineKeyboardMarkup(keyBoard)
    query = update.callback_query.message
    reply = list()
    count = 0
    for data in instaContainer.models:
        reply.append("Login: %s" % data)
        reply.append(instaContainer.models[data].toStr())
        count += 1
        if count % 3 == 0:
            context.bot.send_message(update.callback_query.message.chat_id,
                                     text='\n'.join(reply))
            reply = list()
    context.bot.send_message(update.callback_query.message.chat_id,
                             'Оновити?',
                             reply_markup=markUp)


def main():
    log = 1


def setBot(bot):
    print("bot setted")
    global tgBot
    tgBot = bot


def getBot():
    return tgBot


def start():
    updater = Updater(
        '5277046408:AAH_C8fFsOiTwI9In3aNYqB79Gy6-7Jf4ZE',
        defaults=Defaults(run_async=True),
    )

    setBot(updater.bot)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.update, echo))
    dp.add_handler(CallbackQueryHandler(showAllUsers))

    updater.start_polling()
    return updater.bot
