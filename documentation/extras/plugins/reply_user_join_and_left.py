'''
Module for announcing both new and left participants.
'''

from config import *

@bot.message_handler(func=lambda m: True, content_types=['new_chat_participant'])
def on_user_joins(message):
    #No need to say welcome to the bot itself...
    if str(message.new_chat_participant.id) == my_bot_id:
        return

    name = message.new_chat_participant.first_name

    #If it has a lastname, we add it!
    if hasattr(message.new_chat_participant, 'last_name') and message.new_chat_participant.last_name is not None:
        name += ' ' + str(message.new_chat_participant.last_name)
        
    #If it has a username, we add it!
    if hasattr(message.new_chat_participant, 'username') and message.new_chat_participant.username is not None:
        name += ' ' + str(message.new_chat_participant.username)

    bot.reply_to(message, 'Bem-vindo ' + str(name) + '!')

@bot.message_handler(func=lambda m: True, content_types=['left_chat_participant'])
def on_user_left(message):
    
    #... neither good-bye!
    if str(message.left_chat_participant.id) == my_bot_id:
        return

    name = message.left_chat_participant.first_name

    if hasattr(message.left_chat_participant, 'last_name') and message.left_chat_participant.last_name is not None:
        name += ' ' + str(message.left_chat_participant.last_name)


    if hasattr(message.left_chat_participant, 'username') and message.left_chat_participant.username is not None:
        name += ' ' + str(message.left_chat_participant.username)

    bot.reply_to(message, 'Tchau tchau ' + str(name) + '! (´∩｀。)')

