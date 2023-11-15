key = "6150388707:AAFq4kabad5fzDgk0nF-DWW_E7q3kxXVLJw"

import telebot
import requests
from telebot import types

bot = telebot.TeleBot(key)

info_dict = {
    "Фамилия": "Б",
    "Имя": "О",
    "Пол": "М"
}


@bot.message_handler(commands=['start'])
def hello_world(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Перейти на google", url="https://www.google.by/")
    btn2 = types.InlineKeyboardButton(text="Перейти на onliner", url="https://www.onliner.by/")
    markup.add(btn1)
    markup.add(btn2)
    bot.send_message(message.from_user.id,
                     "По кнопке ниже можно перейти на сайт гугла",
                     reply_markup=markup)


@bot.message_handler(commands=['weather'])
def get_weather(message):
    response = requests.get(
        url="https://api.openweathermap.org/data/2.5/weather?lat=53.9&lon=27.56&appid=e80900febdf285cfc81a051c266a97f8&units=metric")
    desc = response.json()['weather'][0]['description']
    message_text = "В Минске погода: " + desc
    bot.send_message(message.from_user.id, message_text)



@bot.message_handler(commands=['calculate'])
def calculate(message):
    arg = message.text.split(" ")[1]
    result = eval(arg)

    bot.send_message(message.from_user.id, result)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Расходы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Записать расходы')
        btn2 = types.KeyboardButton('Получить список всех расходов')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Выберите действие', reply_markup=markup)
    elif message.text == 'Записать расходы':
        msg = bot.send_message(message.from_user.id, 'Введите инфо о новом расходе')
        bot.register_next_step_handler(msg, print_expenses)

    elif message.text == 'Получить список всех расходов':
        with open('test.txt', mode='r', encoding='UTF-8') as file:
            for line in file.readlines():
                bot.send_message(message.from_user.id, line)


def print_expenses(message):
    with open('test.txt', mode='a+', encoding='UTF-8') as file:
        file.write(message.text)
    bot.send_message(message.from_user.id, 'Сохранено')


bot.polling(none_stop=True, interval=0)
