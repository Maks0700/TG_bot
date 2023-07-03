import telebot
from telebot import types
import webbrowser
bot = telebot.TeleBot("6360322093:AAGRgi8gYtIOXhUrK3Csx2RM4UE1pgVsafA")


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Посетить веб сайт")
    btn2 = types.KeyboardButton("Удалить фото")
    markup.row(btn1, btn2)
    btn3 = types.KeyboardButton("Изменить текст")
    markup.row(btn3)
    photo = open("E:\\Пашок.jpg", "rb")
    bot.send_photo(message.chat.id, photo, reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == "Посетить веб сайт":
        markup = types.InlineKeyboardMarkup()
        website = markup.add(types.InlineKeyboardButton(
            "Посетить веб сайт", url="https://yandex.ru/search/?text=%D0%9A%D0%B8%D0%BB%D0%BB%D0%B8%D0%B0%D0%BD+%D0%9C%D0%B5%D1%80%D1%84%D0%B8&lr=10754&clid=2411726&noreask=1&ento=0oCgpydXcxNDI5NDg1EhJydXcyMDQzOTc6Y3VzdG9tOjAYAnol0JrQuNC90L7QsNC60YLRkdGA0Ysg0JjRgNC70LDQvdC00LjQuFvVfX0"))
        markup.row(website)
        bot.send_message(message.chat.id, website)
    elif message.text == "Удалить фото":
        bot.send_message(message.chat.id, "Deleted")
    elif message.text == "Изменить текст":
        bot.send_message(message.chat.id, "Edited")


bot.polling(none_stop=True)
