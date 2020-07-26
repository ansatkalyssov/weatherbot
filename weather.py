from telebot import types
import requests
import telebot

bot = telebot.TeleBot('1329185471:AAGwO6w7BEey0WRRCP5kCgXvGuADfEyqXmk')


@bot.message_handler(content_types=['start'])
def handle_start(message):
    bot.send_message(message.from_user.id, 'Приветсвуем вас в нашем погода-боте города Ярославль')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    keyboard = types.InlineKeyboardMarkup()
    key_today = types.InlineKeyboardButton(text='Погода на сегодня', callback_data='today')
    keyboard.add(key_today)
    key_tomorrow = types.InlineKeyboardButton(text='Погода на завтра', callback_data='tomorrow')
    keyboard.add(key_tomorrow)
    key_tuesday = types.InlineKeyboardButton(text='Погода на 28.07.2020', callback_data='tuesday')
    keyboard.add(key_tuesday)
    key_wednesday = types.InlineKeyboardButton(text='Погода на 29.07.2020', callback_data='wednesday')
    keyboard.add(key_wednesday)
    key_thursday = types.InlineKeyboardButton(text='Погода на 30.07.2020', callback_data='thursday')
    keyboard.add(key_thursday)
    key_friday = types.InlineKeyboardButton(text='Погода на 31.08.2020', callback_data='friday')
    keyboard.add(key_friday)
    key_saturday = types.InlineKeyboardButton(text='Погода на 1.08.2020', callback_data='saturday')
    keyboard.add(key_saturday)
    key_sunday = types.InlineKeyboardButton(text='Погода на 2.08.2020', callback_data='sunday')
    keyboard.add(key_sunday)

    bot.send_message(message.from_user.id, text='Приветствуем вас в нашем погода-боте города Ярославль!!! \nПогоду на какой день вы хотите узнать ?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'today':
        r = requests.get(
            "https://api.openweathermap.org/data/2.5/onecall?lat=57.63&lon=39.87&exclude=hourly&appid=15f4c7c830b1e5066732786257cf48d2")
        data = r.json()
        temp = data['daily'][0]['temp']['day']
        pressure = data['daily'][0]['pressure']
        humidity = data['daily'][0]['humidity']
        wind_speed = data['daily'][0]['wind_speed']
        bot.send_message(call.message.chat.id, 'Температура на СЕГОДНЯ: {} C \nДавление: {} мм рт.ст. '
                                                   '\nОтносительная влажность: {} % \nСкорость ветра: {} м/с'.format(
                int(temp - 273.15), pressure, humidity, wind_speed))

    elif call.data == 'tomorrow':
        r = requests.get(
            "https://api.openweathermap.org/data/2.5/onecall?lat=57.63&lon=39.87&exclude=hourly&appid=15f4c7c830b1e5066732786257cf48d2")
        data = r.json()
        temp = data['daily'][1]['temp']['day']
        pressure = data['daily'][1]['pressure']
        humidity = data['daily'][1]['humidity']
        wind_speed = data['daily'][1]['wind_speed']
        bot.send_message(call.message.chat.id, 'Температура на ЗАВТРА: {} C \nДавление: {} мм рт.ст. '
                                               '\nОтносительная влажность: {} % \nСкорость ветра: {} м/с'.format(
            int(temp - 273.15), pressure, humidity, wind_speed))

    elif call.data == 'tuesday':
        r = requests.get(
            "https://api.openweathermap.org/data/2.5/onecall?lat=57.63&lon=39.87&exclude=hourly&appid=15f4c7c830b1e5066732786257cf48d2")
        data = r.json()
        temp = data['daily'][2]['temp']['day']
        pressure = data['daily'][2]['pressure']
        humidity = data['daily'][2]['humidity']
        wind_speed = data['daily'][2]['wind_speed']
        bot.send_message(call.message.chat.id, 'Температура на 28.07.2020: {} C \nДавление: {} мм рт.ст. '
                                               '\nОтносительная влажность: {} % \nСкорость ветра: {} м/с'.format(
            int(temp - 273.15), pressure, humidity, wind_speed))

    elif call.data == 'wednesday':
        r = requests.get(
            "https://api.openweathermap.org/data/2.5/onecall?lat=57.63&lon=39.87&exclude=hourly&appid=15f4c7c830b1e5066732786257cf48d2")
        data = r.json()
        temp = data['daily'][3]['temp']['day']
        pressure = data['daily'][3]['pressure']
        humidity = data['daily'][3]['humidity']
        wind_speed = data['daily'][3]['wind_speed']
        bot.send_message(call.message.chat.id, 'Температура на 29.07.2020: {} C \nДавление: {} мм рт.ст. '
                                               '\nОтносительная влажность: {} % \nСкорость ветра: {} м/с'.format(
            int(temp - 273.15), pressure, humidity, wind_speed))

    elif call.data == 'thursday':
        r = requests.get(
            "https://api.openweathermap.org/data/2.5/onecall?lat=57.63&lon=39.87&exclude=hourly&appid=15f4c7c830b1e5066732786257cf48d2")
        data = r.json()
        temp = data['daily'][4]['temp']['day']
        pressure = data['daily'][4]['pressure']
        humidity = data['daily'][4]['humidity']
        wind_speed = data['daily'][4]['wind_speed']
        bot.send_message(call.message.chat.id, 'Температура на 30.07.2020: {} C \nДавление: {} мм рт.ст. '
                                               '\nОтносительная влажность: {} % \nСкорость ветра: {} м/с'.format(
            int(temp - 273.15), pressure, humidity, wind_speed))

    elif call.data == 'friday':
        r = requests.get(
            "https://api.openweathermap.org/data/2.5/onecall?lat=57.63&lon=39.87&exclude=hourly&appid=15f4c7c830b1e5066732786257cf48d2")
        data = r.json()
        temp = data['daily'][5]['temp']['day']
        pressure = data['daily'][5]['pressure']
        humidity = data['daily'][5]['humidity']
        wind_speed = data['daily'][5]['wind_speed']
        bot.send_message(call.message.chat.id, 'Температура на 31.07.2020: {} C \nДавление: {} мм рт.ст. '
                                               '\nОтносительная влажность: {} % \nСкорость ветра: {} м/с'.format(
            int(temp - 273.15), pressure, humidity, wind_speed))

    elif call.data == 'saturday':
        r = requests.get(
            "https://api.openweathermap.org/data/2.5/onecall?lat=57.63&lon=39.87&exclude=hourly&appid=15f4c7c830b1e5066732786257cf48d2")
        data = r.json()
        temp = data['daily'][6]['temp']['day']
        pressure = data['daily'][6]['pressure']
        humidity = data['daily'][6]['humidity']
        wind_speed = data['daily'][6]['wind_speed']
        bot.send_message(call.message.chat.id, 'Температура на 1.08.2020: {} C \nДавление: {} мм рт.ст. '
                                               '\nОтносительная влажность: {} % \nСкорость ветра: {} м/с'.format(
            int(temp - 273.15), pressure, humidity, wind_speed))

    elif call.data == 'sunday':
        r = requests.get(
            "https://api.openweathermap.org/data/2.5/onecall?lat=57.63&lon=39.87&exclude=hourly&appid=15f4c7c830b1e5066732786257cf48d2")
        data = r.json()
        temp = data['daily'][7]['temp']['day']
        pressure = data['daily'][7]['pressure']
        humidity = data['daily'][7]['humidity']
        wind_speed = data['daily'][7]['wind_speed']
        bot.send_message(call.message.chat.id, 'Температура на 2.08.2020: {} C \nДавление: {} мм рт.ст. '
                                               '\nОтносительная влажность: {} % \nСкорость ветра: {} м/с'.format(
            int(temp - 273.15), pressure, humidity, wind_speed))


bot.polling(none_stop=True, interval=0)
