'''
Reply with a random hello.
(first plugin)
'''

import random

from config import *

@bot.message_handler(commands=['oi'])
def reply_oi(message):
    bot.reply_to(message, get_random_hello())

def get_random_hello():
    respostas = ['Oie... ( ˘ ³˘)♥', 'Oi ( ・ω・)∩',
                 'Oi oi oi! (⌒▽⌒)☆', 'Hoy peixe boi (*^▽^*)',
                 'Tudo bem...? (っ˘з(˘⌣˘ )', 'Olá... (´∀｀)♡',
                 'Oi!!! ＼(^▽^＠)ノ', 'Oieeee! ヽ(＾Д＾)ﾉ']
    return random.sample(respostas, 1)

help_commands['oi'] = 'Mando-te um oi! (っ˘з(˘⌣˘ )'
