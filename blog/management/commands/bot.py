import telebot
from django.core.management.base import BaseCommand
from django.conf import settings
from telebot import types
from threading import Thread
import json

class AllowedUser:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def __init__(self, id, page):
        self.id = id
        self.page = page

allowedUsers = []

def isAllowed(id):
    for user in allowedUsers:
        if(user.id == id):
            return True
        return False

bot = telebot.TeleBot("5277046408:AAH_C8fFsOiTwI9In3aNYqB79Gy6-7Jf4ZE", parse_mode=None)

class Command(BaseCommand):
    help = "tg-bot"
    def handle(self, *args, **options):
        allowedFile = open("allowed_users.txt", 'r')
        data = json.loads(allowedFile.read())
        for user in data:
            allowedUsers.append(AllowedUser(user['id'], user['page']))
        print("started")
        thread = Thread(target=bot.infinity_polling())
        thread.start()

@bot.message_handler(commands=['start'])
def AllCommands(message : types.Message):
    markUp = types.InlineKeyboardMarkup()
    showAllUsers = types.InlineKeyboardButton('Показати всіх користувачів',
                                              callback_data='Show all users')
    markUp.row(showAllUsers)
    bot.send_message(message.chat.id, "Головна сторінка",reply_markup=markUp)

@bot.callback_query_handler(func=lambda call: call.data == 'Show all users')
def query1(call: types.CallbackQuery):
    bot.send_message(call.message.chat.id, '123')

@bot.message_handler(content_types=['text'])
def echo_all(message : types.Message) :
    if(isAllowed(message.chat.id) == False):
        bot.send_message(message.chat.id, "Ви не зареєстровані (#%s)" % message.chat.id)
    else:
        bot.send_message(message.chat.id, "Ви зареєстровані (#%s)" % message.chat.id)

@bot.callback_query_handler(func=lambda call: call.data == '1')
def query1(call: types.CallbackQuery):
    bot.send_message(call.message.chat.id, '123')
