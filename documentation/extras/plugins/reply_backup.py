'''
Sends everything saved for backup porpuses.
'''

from config import *
import time

@bot.message_handler(commands=['backup'])
def reply_backup(message):
    for x in hw_levels:
        bot.send_document(message.chat.id, hw_levels[x])
        time.sleep(1)