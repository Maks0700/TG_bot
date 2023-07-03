import telebot
from telebot import types
import webbrowser
bot = telebot.TeleBot("6360322093:AAGRgi8gYtIOXhUrK3Csx2RM4UE1pgVsafA")

@bot.message_handler(content_types=["text"])
def on_click(message):
    if message.text == "Посетить веб сайт":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Перейти на веб сайт", url="https://vk.com/audios184956553"))
        bot.send_message(message.chat.id,"Прошу на сайт",reply_markup=markup)
    elif message.text == "Удалить фото":
        bot.send_message(message.chat.id, "Deleted")
    elif message.text == "Изменить текст":
        bot.send_message(message.chat.id, "Edited")


@bot.message_handler(content_types=["photo"])
def photo(message):
    markup=types.InlineKeyboardMarkup()
    btn1=types.InlineKeyboardButton("Прошу перейдите на сайт",url="https://vk.com/audios184956553")
    markup.row(btn1)
    btn2=types.InlineKeyboardButton("Удалить фото",callback_data="delete")
    btn3=types.InlineKeyboardButton("Изменить текст",callback_data="edit")
    markup.row(btn2,btn3)
    bot.reply_to(message,"Ваааууу какое крутое фото!!!!",reply_markup=markup)

@bot.callback_query_handler(func=lambda callback:True)
def callback_reply(callback):
    if callback.data=="delete":
        bot.delete_message(callback.message.chat.id,callback.message.message_id-2)#Удаляем фотку предыдущую
    elif callback.data=="edit":
        bot.edit_message_text("Измененный текст",callback.message.chat.id,callback.message.message_id)
    
@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Посетить веб сайт")
    btn2 = types.KeyboardButton("Удалить фото")
    markup.row(btn1, btn2)
    btn3 = types.KeyboardButton("Изменить текст")
    markup.row(btn3)
    bot.send_message(message.chat.id, f"Привет {message.from_user.first_name}", reply_markup=markup)




bot.polling(none_stop=True)
