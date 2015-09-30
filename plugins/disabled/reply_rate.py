'''
Asks the user to rate the bot.
'''

from config import *

@bot.message_handler(commands=['rate'])
def reply_rate(message):
    bot.reply_to(message, 'Remember to rate fairly!( ˘ ³˘)♥\nhttp://storebot.me/bot/')

help_commands['rate'] = 'Rate me please! <3'

