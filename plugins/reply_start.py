'''
Warm welcome with help commands!
Also adds new users to regular_users dict().
'''

from config import *
from plugins.reply_help import reply_help_list

@bot.message_handler(commands=['start'])
def reply_start(message):
    cid = get_user_id(message)
    #If user is new, then add him as subscriber!
    if cid not in regular_users:
        add_key_dict(regular_users_file, regular_users, cid, '')
    bot.send_message(message.chat.id, 'Welcome cutie! ( ˘ ³˘)♥')
    reply_help_list(message)
