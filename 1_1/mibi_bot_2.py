import telebot
import requests
from telebot import types

key = '6150388707:AAFq4kabad5fzDgk0nF-DWW_E7q3kxXVLJw'
bot = telebot.TeleBot(key)


@bot.message_handler(commands=['start'])
def start(message):
    mess = f"Привет,<b>{message.from_user.first_name} <u>{message.from_user.last_name}</u> </b> пропиши " \
           f"в строке <b> /menu</b> и или нажми на нее"
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['website'])
def get_user_text(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="тут ссылка на предыдущее задание",
                                      url="https://fakerapi.it/api/v1/credit_cards?_quantity=2/")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "есть возможноть перейдите на сайт", reply_markup=markup)


@bot.message_handler(commands=['menu'])
def get_user_text(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    website = types.KeyboardButton("/website")
    homework = types.KeyboardButton("/homework")
    markup.add(website, homework)
    bot.send_message(message.from_user.id, "вот такое меню", reply_markup=markup)


@bot.message_handler(commands=['homework'])
def get_weather(message):
    response = requests.get(
        url="https://fakerapi.it/api/v1/credit_cards?_quantity=2/")
    desc = response.json()['data'][0]["type"]
    desc1 = response.json()['data'][0]["number"]
    desc2 = response.json()['data'][0]["expiration"]
    desc3 = response.json()['data'][0]["owner"]
    message_text = f"фейковая карта : {desc}  {desc1}  {desc2}  {desc3}"
    bot.send_message(message.from_user.id, message_text)


bot.polling(none_stop=True, interval=0)
