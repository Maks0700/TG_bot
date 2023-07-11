import telebot
from telebot import types
import webbrowser
import sqlite3 as sq
bot = telebot.TeleBot("6360322093:AAGRgi8gYtIOXhUrK3Csx2RM4UE1pgVsafA")


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn_db1 = types.KeyboardButton("Хочешь узнать что-то новое?")
    btn_db2 = types.KeyboardButton("Неинтересно!!")
    markup.row(btn_db1, btn_db2)
    bot.send_message(message.chat.id, "Добро пожаловать!!",
                     reply_markup=markup)


@bot.message_handler(content_types=["text"])
def on_click(message):
    if message.text == "Хочешь узнать что-то новое?":
        markup = types.InlineKeyboardMarkup()
        photo_btn = types.InlineKeyboardButton(
            "Фотография", callback_data="photo")
        name_btn = types.InlineKeyboardButton("Имя", callback_data="name")
        markup.row(photo_btn, name_btn)
        bot.send_message(message.chat.id, "Выберите действие",
                         reply_markup=markup)
    elif message.text == "Неинтересно!!":
        bot.send_message(
            message.chat.id, "https://dzen.ru/?clid=2411725&yredirect=true")


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    with sq.connect("DB for tg.db") as conn:
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS users(
                    name TEXT NOT NULL,
                    photo BLOB UNIQUE NOT NULL
        ) """)
        if callback.data == "name":
            cur.execute("""INSERT INTO users(name) VALUES (?)""",
                        callback.message.from_user.first_name)


bot.polling(none_stop=True)
