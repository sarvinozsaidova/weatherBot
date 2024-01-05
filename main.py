import telebot
import time
import requests
from dotenv import load_dotenv
import os


load_dotenv()
BOT_TOKEN = os.environ.get('BOT_TOKEN')
WEATHER_TOKEN = os.environ.get('WEATHER_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def say_hello(message):
    bot.reply_to(message, "Bizning ilk botimizga hush kelibsiz!!..")

@bot.message_handler(commands=['weather'])
def get_weather(message):
    holatuz = {"Clear":" musaffo osmon", "Sunny":" quyoshli"}
    city = message.text[9:]
    data = get_full_data(city)
    print(str(data))
    holat = data.get("weather", [])[0].get("main", "xatolik")
    temp = round(data.get("main", {}).get('temp', 0) - 273.15)
    location = data.get("sys", {}).get('country')
    bot.send_message(message.chat.id, f"hozirda {city}da havo {temp} bo'lishi kutulmoqda!..  va joylashuv {location} Havo harorari {holat} ")

@bot.message_handler(func = lambda msg: True)
def reply_msg(message):
    bot.send_message(message.chat.id, message.text)

def get_full_data(city):
    url = WEATHER_TOKEN.format(city)
    response = requests.get(url)
    return response.json()


bot.infinity_polling()