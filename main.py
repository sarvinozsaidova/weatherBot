import telebot
import time
import requests


BOT_TOKEN = '6410658353:AAEcvkKWhY-X2L7yT4N0hVhML7nCkyhXFXM'
WEATHER_TOKEN = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=efd8bed5876a79906b7698216deaec22'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def say_hello(message):
    bot.reply_to(message, "Bizning ilk botimizga hush kelibsiz!!..")

@bot.message_handler(commands=['weather'])
def get_weather(message):
    city = message.text[9:]
    data = get_full_data(city)
    temp = round(data.get("main", {}).get('temp', 0) - 273.15)
    location = data.get("sys", {}).get('country')
    osmon = data["weather"][0]['main']
    bot.send_message(message.chat.id, f"hozirda {city}da havo {temp} bo'lishi kutulmoqda!..  va joylashuv {location} Havo {osmon} ")

@bot.message_handler(func = lambda msg: True)
def reply_msg(message):
    bot.send_message(message.chat.id, message.text)
    # time.sleep(0.006)
    # bot.reply_to(message, str(message.chat.id))
    bot.send_message(message.chat.id, "Sleep tugadi!!!!..")

def get_full_data(city):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=efd8bed5876a79906b7698216deaec22'.format(city)
    response = requests.get(url)
    return response.json()


bot.infinity_polling()