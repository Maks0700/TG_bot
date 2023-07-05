import telebot
from telebot import types
import webbrowser
import sqlite3

bot = telebot.TeleBot("6360322093:AAGRgi8gYtIOXhUrK3Csx2RM4UE1pgVsafA")
name=" "


@bot.message_handler(commands=["start"])
def start(message):
    conn=sqlite3.connect('example.sql')
    cur=conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS cars (
        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER
    )""")
    conn.commit()
    cur.close()
    conn.close()


    bot.send_message(message.chat.id,"Привет, сейчас мы тебя зарегистрируем!Введите свое имя")
    bot.register_callback_query_handler(message,user_name)
   
def user_name(message):
    global name
    name=message.text.strip()
    bot.send_message(message.chat.id,"Введите пароль:")
    bot.register_next_step_handler(message,user_pass)
def user_pass(message):
    password=message.text.strip()
    bot.send_message(message.chat.id,)
    conn=sqlite3.connect("example.sql")
    cur=conn.cursor()
    cur.execute("INSERT INTO users(name,pass) VALUES('%s','%s')"%(name,password))
    conn.commit()
    cur.close()
    conn.close()
    markup=types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Список пользователей",callback_data="users"))
    bot.send_message(message.chat.id,"Пользователь зарегистрирован!!",reply_markup=markup)



bot.polling(none_stop=True)

