import telebot

bot = telebot.TeleBot('7902204141:AAEPAkP4-JhUTiYafnut3X1cVFoCMG7dEAo')
mode = 0

@bot.message_handler(commands=['start'])
def start(mess):
    if mess.from_user.last_name != None:
        bot.send_message(mess.chat.id, f'Привет,{mess.from_user.first_name} {mess.from_user.last_name}! Я Экологист-бот, я помогаю с сортировкой отходов и рассказываю про их разложение, чтобы узнать команды, напишите /help')
    else:
        bot.send_message(mess.chat.id, f'Привет,{mess.from_user.first_name}! Я Экологист-бот, я помогаю с сортировкой отходов и рассказываю про их разложение, чтобы узнать команды, напишите /help')

@bot.message_handler(commands=['help'])
def help(mess):
    bot.send_message(mess.chat.id, 'Мои команды - decomposes - чтобы узнать про разложение материала и sort - чтобы узнать как сортировать материалы.')
    
@bot.message_handler(commands=['decomposes'])
def decomposes(mess):
    global mode
    mode = 1
    bot.send_message(mess.chat.id, f'Введите материал, чтобы узнать сколько он разлагается.')

@bot.message_handler(commands=['sort'])
def decomposes(mess):
    global mode
    mode = 2
    bot.send_message(mess.chat.id, f'Введите материал, чтобы узнать как его сортировать')

@bot.message_handler()
def text(mess):
    global mode
    if mode == 1:
        if mess.text.lower() == 'стекло':
            bot.send_photo(mess.chat.id, 'https://smola20.ru/upload/medialibrary/137/1379b9af7d7c1bbd26e862ee78bb7996.jpg')
            bot.send_message(mess.chat.id, 'Стекло разлагается более 1000 лет.')

        elif mess.text.lower() == 'пища':
            bot.send_photo(mess.chat.id, 'https://www.nordicpack.com/wp-content/uploads/hero-livsmedelstillverkning.jpg')
            bot.send_message(mess.chat.id, 'Пищевые отходы разлагаются 2-4 недели.')

        elif mess.text.lower() == 'полиэтиленовые пакеты':
            bot.send_photo(mess.chat.id, 'https://static.tildacdn.com/tild3835-6338-4138-b733-346631356563/20170724175517571863.jpg')
            bot.send_message(mess.chat.id, 'Полиэтиленовые пакеты разлагаются от 100 до 200 лет.')

        elif mess.text.lower() == 'пластик':
            bot.send_photo(mess.chat.id, 'https://uventaplastiktara.ru/resources/images/%D0%9F%D0%BE%D0%BB%D0%B8%D0%BF%D1%80%D0%BE%D0%BF%D0%B8%D0%BB%D0%B5%D0%BD%20%D1%82%D0%B0%D1%80%D0%B0.jpg')
            bot.send_message(mess.chat.id, 'Пластмассовые изделия разлагаются от 6 месяцев до 700 лет')

        elif mess.text.lower() == 'бумага':
            bot.send_photo(mess.chat.id, 'https://tze1.ru/upload/iblock/910/bv9o71siict2fu3wco28sb1rnq1n6juy/artbumaga.jpg')
            bot.send_message(mess.chat.id, 'Бумага разлагается 2 года.')

        elif mess.text.lower() == 'батарейки':
            bot.send_photo(mess.chat.id, 'https://avatars.mds.yandex.net/i?id=0a6d46d64bfc3302cd2314db9bde49d1_l-5356399-images-thumbs&n=13')
            bot.send_message(mess.chat.id, 'Электрические батарейки разлагаются до 100 лет.')

        elif mess.text.lower() == 'доски':
            bot.send_photo(mess.chat.id, 'https://st42.stpulscen.ru/images/product/467/868/303_original.jpeg')
            bot.send_message(mess.chat.id, 'Доски деревянные разлагаются до 10 лет.')

        elif mess.text.lower() == 'алюминий':
            bot.send_photo(mess.chat.id, 'https://static.tildacdn.com/tild3231-3166-4562-b433-623838353564/1a4d7472f257fd50bf90.jpg')
            bot.send_message(mess.chat.id, 'Алюминиевые банки разлагаются 500 лет.')

        elif mess.text.lower() == 'железо':
            bot.send_photo(mess.chat.id, 'https://ron.ucoz.ru/images/posuda/po1.jpg')
            bot.send_message(mess.chat.id, 'Железо разлагается до 10 лет.')

        elif mess.text.lower() == 'жестяная банка':
            bot.send_photo(mess.chat.id, 'https://avatars.mds.yandex.net/i?id=9dcba70ac7d5fc7a67c6432dfaed5657c587b782-4705461-images-thumbs&n=13')
            bot.send_message(mess.chat.id, 'Жестяная банка разлагается до 90 лет.')

> Horie:
elif mess.text.lower() == 'картонные коробки':
            bot.send_photo(mess.chat.id, 'https://avatars.mds.yandex.net/i?id=178b8b22adcb94d00ab47410d01fe6a7_l-6503967-images-thumbs&n=13')
            bot.send_message(mess.chat.id, 'Картонные коробки разлагаются до 1 года')
        
        elif mess.text.lower() == 'одежда':
            bot.send_photo(mess.chat.id, 'https://cdn.lsboutique.ru/files/posts/11.jpg')
            bot.send_message(mess.chat.id, 'Натуральная одежда и ткани разлагаются от 2 до 3 лет')

        

        

    elif mode == 2:
        if mess.text.lower() == 'стекло':
            bot.send_photo(mess.chat.id, 'https://smola20.ru/upload/medialibrary/137/1379b9af7d7c1bbd26e862ee78bb7996.jpg')
            bot.send_message(mess.chat.id, 'Cтекло - выкидывается в синий контейнер для вторсырья, которое в дальнейшем сдается на переработку.')

        elif mess.text.lower() == 'пища':
            bot.send_photo(mess.chat.id, 'https://www.nordicpack.com/wp-content/uploads/hero-livsmedelstillverkning.jpg')
            bot.send_message(mess.chat.id, 'Пища - не нужно сдавать на переработку, выкидывать в отдельный контейнер.')

        elif mess.text.lower() == 'полиэтиленовые пакеты':
            bot.send_photo(mess.chat.id, 'https://static.tildacdn.com/tild3835-6338-4138-b733-346631356563/20170724175517571863.jpg')
            bot.send_message(mess.chat.id, 'Полиэтиленовые пакеты - не стоит сдавать на переработку, т.к. не все виды пластика подлежат повторной переработке.')

        elif mess.text.lower() == 'пластик':
            bot.send_photo(mess.chat.id, 'https://uventaplastiktara.ru/resources/images/%D0%9F%D0%BE%D0%BB%D0%B8%D0%BF%D1%80%D0%BE%D0%BF%D0%B8%D0%BB%D0%B5%D0%BD%20%D1%82%D0%B0%D1%80%D0%B0.jpg')
            bot.send_message(mess.chat.id, 'Пластик - не стоит сдавать на переработку, т.к. не все виды пластика подлежат повторной переработке.')

        elif mess.text.lower() == 'бумага':
            bot.send_photo(mess.chat.id, 'https://tze1.ru/upload/iblock/910/bv9o71siict2fu3wco28sb1rnq1n6juy/artbumaga.jpg')
            bot.send_message(mess.chat.id, 'Бумага - выкидывается в синий контейнер для вторсырья, которое в дальнейшем сдается на переработку.')

        elif mess.text.lower() == 'батарейки':
            bot.send_photo(mess.chat.id, 'https://avatars.mds.yandex.net/i?id=0a6d46d64bfc3302cd2314db9bde49d1_l-5356399-images-thumbs&n=13')
            bot.send_message(mess.chat.id, 'Батарейки - обязательно сдаются на переработку, т.к. выделяют большое кол-во ядовитых веществ.')

        elif mess.text.lower() == 'доски':
            bot.send_photo(mess.chat.id, 'https://st42.stpulscen.ru/images/product/467/868/303_original.jpeg')
            bot.send_message(mess.chat.id, 'Доски - при сдаче на переработку нужно удалять части не подлежащие повторной переработке.')

        elif mess.text.lower() == 'алюминий':
            bot.send_photo(mess.chat.id, 'https://static.tildacdn.com/tild3231-3166-4562-b433-623838353564/1a4d7472f257fd50bf90.jpg')
            bot.send_message(mess.chat.id, 'Алюминий - выкидывается в синий контейнер для вторсырья, которое в дальнейшем сдается на переработку.')

        elif mess.text.lower() == 'железо':
            bot.send_photo(mess.chat.id, 'https://ron.ucoz.ru/images/posuda/po1.jpg')
            bot.send_message(mess.chat.id, 'Железо - выкидывается в синий контейнер для вторсырья, которое в дальнейшем сдается на переработку.')

        elif mess.text.lower() == 'жестяная банка':
            bot.send_photo(mess.chat.id, 'https://avatars.mds.yandex.net/i?id=9dcba70ac7d5fc7a67c6432dfaed5657c587b782-4705461-images-thumbs&n=13')
            bot.send_message(mess.chat.id, 'Жестяная банка - выкидывается в синий контейнер для вторсырья, которое в дальнейшем сдается на переработку.')

> Horie:
elif mess.text.lower() == 'картонные коробки':
            bot.send_photo(mess.chat.id, 'https://avatars.mds.yandex.net/i?id=178b8b22adcb94d00ab47410d01fe6a7_l-6503967-images-thumbs&n=13')
            bot.send_message(mess.chat.id, 'Картонные коробки - выкидываются в синий контейнер для вторсырья, которое в дальнейшем сдается на переработку.')
            
        elif mess.text.lower() == 'одежда':
            bot.send_photo(mess.chat.id, 'https://cdn.lsboutique.ru/files/posts/11.jpg')
            bot.send_message(mess.chat.id, 'Одежда - сдается на переработку(обувь в России не принимают на переработку), но лучше отдать вещи нуждающимся.')
            
            
        mode = 0

bot.infinity_polling()
