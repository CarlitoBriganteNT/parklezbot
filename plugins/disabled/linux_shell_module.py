'''
Thanks to https://github.com/JackRendor He is awesome! <3
'''

import subprocess

from config import *

@bot.message_handler(commands=['shell'])
def shell_command(message):
    cid = get_user_id(message)
    
    if cid in admin_users:
        markup = types.ForceReply(selective=False)
        msg = bot.send_message(message.chat.id, 'Send me your command:', reply_markup=markup)
        bot.register_next_step_handler(msg, execute_command)

def execute_command(message):
    bot.send_message(message.chat.id, 'Executing...')
    result_command = subprocess.Popen(message.text, shell=True, stdout=subprocess.PIPE).stdout.read()
    if result_command == '':
        bot.reply_to(message, 'Something went wrong!')
    else:
        bot.send_message(message.chat.id, result_command)

admin_commands['shell'] = 'Runs a command on terminal.'
