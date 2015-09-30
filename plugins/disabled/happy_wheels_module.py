from config import *

hw_levels_file = 'files/happy_wheels.txt'
hw_levels = load_dict(hw_levels_file)

### Core functionality ###
@bot.message_handler(commands=['maps'])
def reply_hw_levels(message):
    msg = message.text[6:]
    
    if msg in hw_levels:
        bot.send_document(message.chat.id, hw_levels[msg])
        return
    
    elif msg.isdigit():
        page = int(msg)
        
    elif msg == '':
        page = 0

    elif msg == 'AndreasBOT':
        page = 0
        
    else:
        bot.reply_to(message, 'Couldn\'t find {!s}! :C'.format(msg))
        return

    ipp = 12 #items per page
    start = ipp * page
    end = start + ipp

    levels_list = sorted(list(hw_levels.keys()))
    list_len = len(levels_list)
    
    #Check if there is enough elements to fill.
    if list_len - start < ipp:
        keys = int(list_len - start)
    else:
        keys = int(ipp)

    cid = get_user_id(message)

    reply_msg = 'Available Levels:\n'
    reply_msg += '==================\n'
    for key in range(keys):
        reply_msg += levels_list[(start+key)] + '\n'
    reply_msg += '=================='
    reply_msg += '\nWrite /maps Level Name to download it.'
    reply_msg += '\nPage nº' + str(page) + ' of ' + str(int(list_len/ipp)) + '.'
    if int(list_len/ipp) > page:
        reply_msg += '\nNext page. = /maps ' + str(page+1)
    bot.send_message(message.chat.id, reply_msg)
    
@bot.message_handler(commands=['delmap'])
def reply_deleted_map(message):
    cid = get_user_id(message)

    if cid in admin_users:
        level_to_find = message.text[8:]
        if level_to_find == '':
            bot.reply_to(message, 'Ex. /delmap Map name')
        elif level_to_find in hw_levels:
            remove_key_dict(hw_levels_file, hw_levels, level_to_find)
            bot.reply_to(message, 'Map deleted! :3')
        else:
            bot.reply_to(message, 'I couldn\'t find this map! :C')

### File Manager ###
@bot.message_handler(func=lambda message: get_file_extention(message) == '.happywheels', content_types=['document'])
def receive_new_level(message):
    cid = get_user_id(message)
    
    file_name, extension = message.document.file_name.split('.')
    
    if extension == 'happywheels':
    
        level_file_id = message.document.file_id
    
        if file_name not in hw_levels:
            add_key_dict(hw_levels_file, hw_levels, file_name, level_file_id)
            bot.reply_to(message, 'Thanks for sharing! <3\nYour level is ready at /maps !')
        else:
            bot.reply_to(message, 'I already have a map with that name, could you edit it at the app?')

help_commands['maps'] = 'List of levels for Happy Wheels.'
admin_commands['delmap'] = 'Deletes a level of Happy Wheels.'

