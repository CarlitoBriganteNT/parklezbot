'''
Reply help_commands list.
'''

from config import *

@bot.message_handler(commands=['help'])
def reply_help_list(message):
    cid = get_user_id(message)
    help_text = 'The following commands are available:\n'
    cmd_list = sorted(list(help_commands.keys()))
    for key in cmd_list:
        help_text += '/' + str(key) + ': ' + str(help_commands[key]) + '\n'
    bot.send_message(message.chat.id, help_text)

#help_commands['help'] = 'List of help commands.'
