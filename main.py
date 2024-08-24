import telebot
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
from gtts import gTTS

get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('bee94f844ebb0be8dd52f08431e25bf0')
mgr = owm.weather_manager()
bot = telebot.TeleBot("5828185551:AAHOBR8QxW3rO29nu_Q4yY4EOgLlGxGrnLU")


@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f"<b>привет {message.from_user.first_name}!</b>\nЭтот бот делает прогноз погоды.             Введите название города"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')


@bot.message_handler(content_types=['text', 'photo'])
def send_echo(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    status = w.detailed_status
    w.wind()
    humidity = w.humidity
    temp = w.temperature('celsius')['temp']
    answer = ("В городе " + message.text + " сейчас " + str(status) + "\nТемпература " + str(
        round(temp)) + " градусов по цельсию;" + "\nВлажность составляет " + str(
        humidity) + "%;" + "\nСкорость ветра " + str(w.wind()['speed']) + " метров в секунду;")

    bot.send_message(message.chat.id, answer, )

    if status == 'ясно':
        file = open('sun.png.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
    if status == 'небольшой проливной дождь':
        file = open('rain1.png', 'rb')
        bot.send_photo(message.chat.id, file)
    if status == 'пасмурно':
        file = open('clouds.png.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
    if status == 'переменная облачность':
        file = open('clouds.png.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
    if status == 'облачно с прояснениями':
        file = open('clouds.png.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
    if status == 'небольшая облачность':
        file = open('clouds.png.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
    if status == 'небольшой дождь':
        file = open('rain1.png', 'rb')
        bot.send_photo(message.chat.id, file)
    if status == 'дождь':
        file = open('rain1.png', 'rb')
        bot.send_photo(message.chat.id, file)

    text_val = answer
    language = 'ru'
    obj = gTTS(text=text_val, lang=language, slow=False)
    obj.save("pogoda.mp3")
    file = open('pogoda.mp3', 'rb')
    bot.send_audio(message.chat.id, file)


bot.infinity_polling()
