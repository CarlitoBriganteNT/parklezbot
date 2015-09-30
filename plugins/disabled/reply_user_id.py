'''
Replies chat's ID.
'''

from config import *

@bot.message_handler(commands=['me'])
def reply_user_id(message):
    if isinstance(message.chat, types.User):
        bot.send_message(message.chat.id, 'Your personal ID is: {0!s}'.format(message.chat.id))

    elif isinstance(message.chat, types.GroupChat):
        bot.send_message(message.chat.id, 'This group\'s ID is: {0!s}\nYour personal ID is: {1!s}'.format(message.chat.id, message.from_user.id))

help_commands['me'] = 'See the chat ID.'
