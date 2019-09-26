# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 12:10:16 2019

@author: avsirotkin
"""
import datetime
import dateparser
import re
import requests
import telebot
import json
from telebot import apihelper
from announce import *

token=open("CTB_token.txt", "rt").read()

from telebot import apihelper
from telebot import types

TG_PROXY = ''
TG_PROXY=open("proxy.txt", "rt").read()

# Set proxy
print(TG_PROXY)
if TG_PROXY != "":
    apihelper.proxy = {'https': TG_PROXY}
#    print("use proxy ", TG_PROXY)
else:
    apihelper.proxy = {}

bot = telebot.TeleBot(token)


command_list = ''''announce', 'объява', 'объявление', 'анонс': обработать пост ЖЖ с анонсами'''


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    print("\n\n Command Message:\n")
    print(message)
#    bot.send_message(message.from_user.id, "Привет! Я бот который научится помогать тебе искать команду или игроков для ЧГК.\nКогда я вырасту, тут будет список команд и много других полезных штук.")
    bot.send_message(message.from_user.id, "Привет! Вот основной список команд:\n"+command_list)

@bot.message_handler(commands=['announce', 'объява', 'объявление', 'анонс'])
def make_announcement(message):
    print("\n\n Command Message legs:\n")
    print(message)
    
    info = message.text.strip().split()
    
    if len(info)>1:
        my_message = get_announcement(info[1])
    else:
        my_message = get_announcement("https://chgk-spb.livejournal.com/2046721.html")
#        my_message = "Не указана ссылка на пост"
    print(my_message)
    bot.send_message(message.from_user.id, my_message, disable_web_page_preview = True, parse_mode="HTML")


bot.polling(none_stop=True, interval=0)


 # Обработчик для документов и аудиофайлов
@bot.message_handler(content_types=['document', 'audio'])
def handle_document_audio(message):
    pass

#while(1):
#    try:
bot.polling(none_stop=True, interval=0, timeout=10)
print("Бываю ли я тут")
#    except:
#        print("Что-то пошло не так.")
