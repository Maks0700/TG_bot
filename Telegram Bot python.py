import telebot
from telebot import types

bot = telebot.TeleBot("6218663006:AAGGboF-ByLwUBn0MUrTNv5kiYrAqzwGA34")


@bot.message_handler(commands=["start", "help"])
def reply_message(message):
    bot.send_message(message.chat.id, message.from_user_first_name)


bot.polling(none_stop=True)
