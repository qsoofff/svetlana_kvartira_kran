import telebot
import random
from passwords import gen_pass   
import orel_ili_reshka

    
bot = telebot.TeleBot("7691393493:AAHXi_5MCuC-6-wE1fDINvikvjz2u9dl4no")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

bot.message_handler(commands=['fliptext'])
def flip_text(message):
    text = message.text.replace('/fliptext ', '')
    bot.reply_to(message, text[::-1])

@bot.message_handler(commands=['ball'])
def magic_ball(message):
    answers = ["Да", "Нет", "Возможно", "Спроси позже", "Точно да!", "Ни в коем случае"]
    bot.reply_to(message, f"🎱 Ответ: {random.choice(answers)}")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['password'])
def send_pass(message):
    bot.reply_to(message, gen_pass(10))

@bot.message_handler(commands=['orelreshka'])
def send_orelreshka(message):
    bot.reply_to(message, orel_ili_reshka)

@bot.message_handler(commands=['secret'])
def send_bye(message):
    print(message)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
print('start')
bot.polling()
