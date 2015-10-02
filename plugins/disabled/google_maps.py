'''
Thanks to https://github.com/ineedblood/telegram-bot

I only converted this to python 3!
'''

import urllib.request, urllib.error, urllib.parse

from config import *

@bot.message_handler(commands=['map'])
def command_map(message):
    token = message.text[5:]
    if token == '':
        bot.reply_to(message, 'Ex. /map Kazakhstan')
    if ' ' in token:
        token = token.replace(' ', '+')
    token = token.encode('utf-8')
    url = "https://maps.googleapis.com/maps/api/staticmap?center=%s&zoom=14&size=400x400&maptype=hybrid&key=AIzaSyBmZVQKUXYXYVpY7l0b2fNso4z82H5tMvE" % token
    urllib.request.urlretrieve(url, "files/map.png")
    bot.send_photo(message.chat.id, open( 'files/map.png', 'rb'))

help_commands['map'] = '[BETA] Get a small visualization of somewhere.'
