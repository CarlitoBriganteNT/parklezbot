'''
This plugin helps to debug code significantly.
As for telegram's ideology, do not use this if you don't want to debug.
Privacy should be number 1 concern.
'''

from config import *

def listener(messages):
    for m in messages:
        try:
            #If we are in a private conversation...
            if isinstance(m.chat, types.User):
                if m.content_type == 'text':
                    count_messages()
                    print(str(m.chat.first_name) + ' [' + str(m.chat.id) + ']: ' + 'on private: ' + repr(m.text))
            #Else if we are in a group...
            elif isinstance(m.chat, types.GroupChat):
                if str(m.chat.id) not in groups_ids:
                    add_key_dict(groups_ids_file, groups_ids, m.chat.id, m.chat.title)

                if m.content_type == 'text':
                    count_messages()
                    print(str(m.from_user.first_name) + ' [' + str(m.from_user.id) +
                          ']: ' + 'on group: [' + str(m.chat.id) + ']: ' + repr(m.text))

        except UnicodeEncodeError as e:
            print(e)
            pass
        
bot.set_update_listener(listener)
