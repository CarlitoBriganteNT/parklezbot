from config import *

sounds_list_file = 'files/sounds.txt'
sounds_list = load_dict(sounds_list_file)

new_sound = dict()

### Core functionality ###
@bot.message_handler(commands=['snd'])
def reply_sound(message):
    sound_to_find = message.text[5:]
    
    if sound_to_find in sounds_list:
        bot.send_voice(message.chat.id, sounds_list[sound_to_find])
        
    else:
        bot.reply_to(message, 'See the list of /snds available! <3')

@bot.message_handler(commands=['delsnd'])
def reply_deleted_sound(message):
    cid = get_user_id(message)
        
    if cid in admin_users:
        sound_to_find = message.text[8:]
        if sound_to_find == '':
            bot.reply_to(message, 'Ex. /delsnd Sound name')
            return
        
        elif sound_to_find in sounds_list:
            remove_key_dict(sounds_list_file, sounds_list, sound_to_find)
            bot.reply_to(message, 'Sound deleted! :3')
        else:
            bot.reply_to(message, 'I coudln\'t find this one! :C')

admin_commands['delsnd'] = 'Deletes a sound.'

@bot.message_handler(commands=['snds'])
def reply_sound_list(message):
    msg = message.text[6:]
    if msg in sounds_list:
        bot.send_voice(message.chat.id, sounds_list[msg])
        return
    
    elif msg.isdigit():
        page = int(msg)
        
    elif msg == '':
        page = 0
        
    elif msg == 'AndreasBOT':
        page = 0
    
    else:
        bot.reply_to(message, 'See the list of /snds available! <3')
        return

    ipp = 12 #items per page
    start = ipp * page
    end = start + ipp

    levels_list = sorted(list(sounds_list.keys()))
    list_len = len(levels_list)
    
    #Check if there is enough elements to fill.
    if list_len - start < ipp:
        keys = int(list_len - start)
    else:
        keys = int(ipp)

    reply_msg = 'Available Sounds:\n'
    reply_msg += '==================\n'
    for key in range(keys):
        reply_msg += levels_list[(start+key)] + '\n'
    reply_msg += '=================='
    reply_msg += '\nWrite /snd Sound Name to receive it.'
    if int(list_len/ipp) > page:
        reply_msg += '\nPage nº' + str(page) + ' of ' + str(int(list_len/ipp)) + '.'
        reply_msg += '\nNext page. = /snds ' + str(page+1)
    bot.send_message(message.chat.id, reply_msg)

help_commands['snds'] = 'Sounds list.'

### File Manager ###
@bot.message_handler(content_types=['voice'])
def receive_new_sound(message):
    cid = get_user_id(message)
    
    if cid in admin_users:
        new_sound[cid] = message.voice.file_id
        markup = types.ForceReply(selective=True)
        msg = bot.reply_to(message, 'What name should I give it?', reply_markup=markup)

        bot.register_next_step_handler(msg, choose_sound_name)

def choose_sound_name(message):
    cid = get_user_id(message)
        
    try:
        msg = message.text
        if msg in sounds_list:
            bot.reply_to(message, 'I already got a sound with that name! :C')
        elif msg == 'cancel':
            return
        else:
            add_key_dict(sounds_list_file, sounds_list, msg, new_sound[cid])
            bot.reply_to(message, 'Sound has been added!')
    except Exception:
        bot.reply_to(message, 'Something went wrong, canceling...')
        pass
