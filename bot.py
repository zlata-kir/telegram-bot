#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import token

bot = telebot.TeleBot(token)

# Handle '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'привет! бонжур! хелло!')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'чем я тебе помогу, братан, я куча пикселей, сходи к психологу.')

@bot.message_handler(commands=['info'])
def send_welcome(message):
    bot.reply_to(message, 'Что я умею? Да понятия не имею, у меня нет самосознания, я не способен к рефлексии, я умею делать то что задумал мой создатель. К сожалению создатель не захотел делать нормальное описание, так что довольствуйтесь этим.')


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_yes":
        bot.answer_callback_query(call.id, "Answer is Yes")
    elif call.data == "cb_no":
        bot.answer_callback_query(call.id, "Answer is No")


@bot.message_handler(func=lambda message: True)
def message_handler(message):
    bot.send_message(message.chat.id, "Yes/no?", reply_markup=gen_markup())


@bot.message_handler(content_types=['photo'])
def send_dice(message):
    bot.send_dice(message.chat.id) # это мой брат написал 


def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Yes", callback_data="cb_yes"),
                               InlineKeyboardButton("No", callback_data="cb_no"))
    return markup

bot.infinity_polling()
