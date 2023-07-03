import telebot
from telebot import types

bot = telebot.TeleBot("6218663006:AAGGboF-ByLwUBn0MUrTNv5kiYrAqzwGA34")
name=" "
surname=" "
age=0
@bot.message_handler(content_types=["text"])
def name(message):
    
    if message.text=="/start":
        bot.send_message(message.chat.id,"И так пожалуй начнем знакомство.Как Вас зовут?")
        bot.register_next_step_handler(message,get_name)
    else:
        bot.send_message(message.chat.id,"Введите еще раз правильную команду")
def get_name(message):
    global name
    name=message.text
    bot.send_message(message.chat.id,"Введите свою фамилию")
    bot.register_next_step_handler(message,get_surname)
def get_surname(message):
    global surname
    surname=message.text
    bot.send_message(message.chat.id,"Введите свой возраст")
    bot.register_next_step_handler(message,get_age)
def get_age(message):
    global age
    while age==0:
        try:
            age=int(message.text)
        except Exception:
            bot.send_message(message.chat.id,"Цифрами пожалуйста")
    markup=types.InlineKeyboardMarkup()
    markup_yes=types.InlineKeyboardButton("Да",callback_data="yes")
    markup_no=types.InlineKeyboardButton("Нет",callback_data="no")
    markup.add(markup_yes,markup_no)
    question="Тебе "+str(age)+" лет, зовут тебя "+name+" "+f"{ surname} ?"
    bot.send_message(message.chat.id,question,reply_markup=markup)


@bot.callback_query_handler(func=lambda callback:True)
def state(callback):
    if callback.data =="yes":
        bot.edit_message_text("Запомню :) ",callback.message.chat.id,callback.message.message_id)
    elif callback.data=="no":
        bot.edit_message_text("Введите заново информацию!!",callback.message.chat.id,callback.message.message_id)


    # elif callback.text=="no":


    




bot.polling(none_stop=True)
