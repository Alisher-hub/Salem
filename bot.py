import telebot
from telebot import types
import json
import config
import requests
import shutil
import random

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def bot_start(msg):
    bot.send_message(msg.chat.id, f'Привет, {msg.chat.first_name}! Меня зовут Вася!')
    main_menu(msg)

def main_menu(msg):
    
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
#     help_btn = types.KeyboardButton('Помощь')
#     topic_btn = types.KeyboardButton('Раздел')
#     keyboard.row(topic_btn, help_btn)
    
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width=1)
    keyboard.add(* [types.KeyboardButton(name) for name in ['\ud83d\udd19 Топ услуги', 'Раздел', 'Помощь']])
    

    bot.send_message(msg.chat.id, 'Вы в главном меню. Выберите раздел:', reply_markup=keyboard)

    bot.register_next_step_handler(choose_step_0, msg)
    
def choose_step_0(msg):
    print (msg)
    if 'Помощь' in msg.text:
        bot.send_message(msg.chat.id, 'Сорян, но мне грустно!')
        r = requests.get(f'https://picsum.photos/200/300', stream = True)
        
        with open ('img.png', 'wb') as out_file:
            shutil.copyfileobj(r.raw, out_file)
            bot.send_photo(msg.chat.id, out_file)
        del r
        
        photo = open('img.png', 'rb')
        bot.send_photo(msg.chat.id, photo)
        
        main_menu(msg)
        
    elif msg.text == 'Раздел':
        pass
    
    else:
        bot.send_message(msg.chat.id, 'Кажется что-то не так!')
        main_menu(msg)

if __name__ =='__main__':
    bot.polling(none_stop=True)