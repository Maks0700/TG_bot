import telebot
from telebot import types

bot = telebot.TeleBot("6218663006:AAGGboF-ByLwUBn0MUrTNv5kiYrAqzwGA34")


@bot.message_handler(commands=["start"])
def buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    photo = types.KeyboardButton("Получить открытку")
    audio = types.KeyboardButton("Послушать музыку")
    video = types.KeyboardButton("Посмотреть видос")
    markup.add(audio, photo, video)
    bot.send_message(
        message.chat.id, f"Привет {message.from_user.first_name}, я тестовый бот от Макса. Прошу выбрать нажатие кнопки", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def reply(message):

    if message.text == "Посмотреть видос":
        video = open("E:\\Для бота.mp4", "rb")
        bot.send_video(
            message.chat.id, video)

    elif message.text == "Получить открытку":
        photo = open("E:\\Пашок.jpg", "rb")
        bot.send_photo(
            message.chat.id, photo)

    elif message.text == "Послушать музыку":
        audio = open("E:\\Инста.mp3", "rb")
        bot.send_audio(message.chat.id, audio)

    else:
        while True:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button_zaeb = types.KeyboardButton(
                "Нажми,чтобы все это закончилось")
            markup.add(button_zaeb)
            bot.send_message(message.chat.id, "Hello", reply_markup=markup)
            if message.text == "Нажми,чтобы все это закончилось":
                break


bot.polling(none_stop=True)
