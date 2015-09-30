'''
Reply stats.
'''

from config import *

#from plugins.happy_wheels_module import hw_levels
#from plugins.sounds_module import sounds_list
#from plugins.anime_module import animes_list

@bot.message_handler(commands=['stats'])
def reply_stats(message):

    reply_text = 'Subscribers: ' + str(len(regular_users))
    reply_text += '\nGroups: ' + str(len(groups_ids))
#    reply_text += '\nAnimes: ' + str(len(animes_list))
#    reply_text += '\nSons: ' + str(len(sounds_list))
#    reply_text += '\nMapas de Happy Wheels: ' + str(len(hw_levels))

    bot.send_message(message.chat.id, reply_text)

help_commands['stats'] = 'See my stats.'
