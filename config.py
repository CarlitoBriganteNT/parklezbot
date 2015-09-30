#####################################

token = ''

#####################################

import telebot

from telebot import types

bot = telebot.TeleBot(token)

bot_info = bot.get_me()

for key, val in bot_info.__dict__.items():
    print(str(key) + ': ' + str(val))

from plugins.common_functions import *

##################################
# Here comes our amateur databases

help_commands = dict()
admin_commands = dict()

#Localization (in case you want to customize it)

admin_users_file = 'data/admins.txt'
groups_ids_file = 'data/groups.txt'
regular_users_file = 'data/users.txt'

#Load dictionaries for every plugin

admin_users = load_dict(admin_users_file)
#Add yourself as an admin. admin_users[ID] = 'Your name just for reference'
admin_users[12345678] = 'Example of how to add admin'
save_dict(admin_users_file, admin_users)

groups_ids = load_dict(groups_ids_file)
regular_users = load_dict(regular_users_file)

