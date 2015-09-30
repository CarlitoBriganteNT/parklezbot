'''
With this plugin, you could save every new user with a name,
so then, you could make functions like 'addadmin' automatically
get user's name!

However, It's really useless.
'''

from config import *

def get_best_name(message):
    'Returns the best name reference for a new user. @Username > First + Last name > First name'
    if isinstance(message.chat, types.User):
        if hasattr(message.chat, 'last_name') and message.chat.last_name is not None:
            name_reference = str(message.chat.first_name) + ' ' + str(message.chat.last_name)
            
        if hasattr(message.chat, 'username') and message.chat.username is not None:
            name_reference = '@' + str(message.chat.username)
            
        else:
            name_reference = str(message.chat.first_name)

    if isinstance(message.chat, types.GroupChat):
        if hasattr(message.from_user, 'last_name') and message.from_user.last_name is not None:
            name_reference = str(message.from_user.first_name) + ' ' + str(message.from_user.last_name)
            
        if hasattr(message.from_user, 'username') and message.from_user.username is not None:
            name_reference = '@' + str(message.from_user.username)
            
        else:
            name_reference = str(message.from_user.first_name)

    return name_reference
