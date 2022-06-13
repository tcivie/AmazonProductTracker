"""
@author Gleb Tcivie
An application that checks from the list of the products if some price or aviability has changed and notifies via Telegram bot
"""

import telebot
import json

with open('Credentials') as file:
    credentials = json.load(file)
bot = telebot.TeleBot(credentials['TOKEN'], parse_mode=None)  # You can set parse_mode by default. HTML or MARKDOWN


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
