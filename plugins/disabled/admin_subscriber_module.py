'''
Channel features should be implemented when it's available.
'''

from config import *

import time

@bot.message_handler(commands=['stop'])
def reply_announcements_keyboard(message):
    cid = get_user_id(message)
    if cid in regular_users:
        remove_key_dict(regular_users_file, regular_users, cid)
        bot.reply_to(message, 'I won\'t bother you anymore... (´Д｀。)\nif you change your mind, you can /subscribe anytime ( ˘ ³˘)♥!')

@bot.message_handler(commands=['subscribe'])
def subscribe_user(message):
    cid = get_user_id(message)
    if cid in regular_users:
        bot.reply_to(message, 'You\'re already subbed cutie! ( ˘ ³˘)♥')
        return
        
    else:
        bot.reply_to(message, 'Thanks for resubbing!\n(ɔˆ ³(ˆ⌣ˆc)\nYou\'ll be notified, I promess not to bother!')
        add_key_dict(regular_users_file, regular_users, cid, '')
        return
        
help_commands['stop'] = 'Stops notifications!'
help_commands['subscribe'] = 'Receive news about the bot!'

@bot.message_handler(commands=['post'])
def admin_announce_subscribers(message):
    cid = get_user_id(message)

    if cid in admin_users:
        markup = types.ForceReply(selective=True)
        replymsg = bot.reply_to(message, 'What shall I notify the subscribers?\n/cancel to stop the operation!', reply_markup=markup)
        bot.register_next_step_handler(replymsg, admin_announce_subscribers_step)

def admin_announce_subscribers_step(message):
    cid = get_user_id(message)
    
    lista = []
    for user in regular_users.keys():
        lista.append(user)

    text = message.text
    if text == '/cancel':
        return
        
    else:
        for user in lista:
            try:
                bot.send_message(user, text)
                time.sleep(0.1)
            except telebot.apihelper.ApiException:
                remove_key_dict(regular_users_file, regular_users, user)
                print('User:', user, 'blocked/kicked us! Removing him...')

admin_commands['post'] = 'Post something to the subs (text only).'
