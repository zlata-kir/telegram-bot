import os
import telebot
import random, requests
from config import token
bot = telebot.TeleBot(token)
# Handle '/start'
#https://random.dog/woof.json
def get_dog_image_url():    
        url = 'https://random.dog/woof.json'
        res = requests.get(url)
        data = res.json()
        return data['url']
def get_duck_image_url():    
        url = 'https://random-d.uk/api/random'
        res = requests.get(url)
        data = res.json()
        return data['url']
       
@bot.message_handler(commands=['duck'])
def duck(message):
    '''По команде duck вызывает функцию get_duck_image_url и отправляет URL изображения утки'''
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)

@bot.message_handler(commands=['dog'])
def dog(message):
    image_url = get_dog_image_url()
    bot.reply_to(message, image_url)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'привет! бонжур! хелло!')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'чем я тебе помогу, братан, я куча пикселей, сходи к психологу.')

@bot.message_handler(commands=['info'])
def send_welcome(message):
    bot.reply_to(message, 'Что я умею? Да понятия не имею, у меня нет самосознания, я не способен к рефлексии, я умею делать то что задумал мой создатель. К сожалению создатель не захотел делать нормальное описание, так что довольствуйтесь этим.')

@bot.message_handler(content_types=['photo'])
def send_sticker(message):
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEugZ9nEjsF5BO9q2rpCYv8Vc5JPyILiAACaRMAAsNvEEp0UMRQ1rOWsjYE")

@bot.message_handler(commands=['dice'])
def send_dice(message):
    bot.send_dice(message.chat.id)
                 
@bot.message_handler(commands=['mem'])
def send_mem(message):
    with open('images/mem1.jpeg', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

@bot.message_handler(commands=['meme'])
def send_mem(message):
    ing_name = random.choice(os.listdir("images"))
    with open(f'images/{ing_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["oldmem"]) 
def send_mem(message):
    number = random.randint(1,100)
    if 25 <= number:
        old_mem = random.choice(os.listdir('images2'))
        bot.send_message(message.chat.id, "Вам попался ОБЫЧНЫЙ МЕМ...")
        with open (f'images2/{old_mem}', 'rb') as f:
            bot.send_photo(message.chat.id, f)
    elif 25 > number and 1 < number:
        old_mem = random.choice(os.listdir('images3'))
        bot.send_message(message.chat.id, "Вам попался РЕДКИЙ МЕМ!")
        with open (f'images3/{old_mem}', 'rb') as f:
            bot.send_photo(message.chat.id, f)
    elif 1 == number:
        old_mem = random.choice(os.listdir('legendary'))
        bot.send_message(message.chat.id, "Вам попался ЛЕГЕНДАРНЫЙ МЕМ!!!")
        with open (f'legendary/{old_mem}', 'rb') as f:
            bot.send_photo(message.chat.id, f)


bot.infinity_polling()
