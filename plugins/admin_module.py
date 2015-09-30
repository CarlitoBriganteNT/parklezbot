'''
This module gives some special admin functionality.
'''
from config import *

temp_id = dict()

@bot.message_handler(commands=['admin'])
def reply_admin_commands_list(message):
    'Replies admin_commands dict'
    cid = get_user_id(message)

    if cid in admin_users:
        help_text = 'The following commands are available:\n'
        cmd_list = sorted(list(admin_commands.keys()))
        for key in cmd_list:
            help_text += '/' + str(key) + ': ' + str(admin_commands[key]) + '\n'
        bot.send_message(cid, help_text)

@bot.message_handler(commands=['addadmin'])
def reply_add_admin_cmd(message):
    'adds an admin'
    cid = get_user_id(message)
        
    if cid in admin_users:
        id_to_add = message.text[10:]
        
        if id_to_add == '':
            markup = types.ForceReply(selective=True)
            replymsg = bot.reply_to(message, 'What\'s the new admin\'s ID?\n/cancel to stop the operation!', reply_markup=markup)
            bot.register_next_step_handler(replymsg, add_admin_step_id)

        elif id_to_add.isdigit() == False:
            bot.reply_to(message, 'Ex. /addadmin 1234567')
            return

        elif id_to_add.isdigit():
            temp_id[cid] = int(id_to_add)
            markup = types.ForceReply(selective=True)
            replymsg = bot.reply_to(message, 'What\'s the new admin\'s name?\n/cancel to stop the operation!', reply_markup=markup)
            bot.register_next_step_handler(replymsg, add_admin_step_name)

def add_admin_step_id(message):
    cid = get_user_id(message)

    id_to_add = message.text
    if id_to_add == '/cancel':
        return
    
    elif id_to_add.isdigit():
        temp_id[cid] = int(id_to_add)
        markup = types.ForceReply(selective=True)
        replymsg = bot.reply_to(message, 'What\'s the new admin\'s name?\n/cancel to stop the operation!', reply_markup=markup)
        bot.register_next_step_handler(replymsg, add_admin_step_name)

def add_admin_step_name(message):
    cid = get_user_id(message)
    
    new_name = message.text
    if new_name == '/cancel':
        return
    
    else:
        markup = types.ReplyKeyboardHide(selective=True)
        add_key_dict(admin_users_file, admin_users, temp_id[cid], new_name)
        bot.reply_to(message, 'New admin!ヽ(*⌒∇⌒*)ﾉ\n', reply_markup=markup)

admin_commands['addadmin'] = 'Adds admin by ID.'

@bot.message_handler(commands=['deladmin'])
def reply_del_admin_cmd(message):
    'Deletes an admin'
    cid = get_user_id(message)
        
    if cid in admin_users:
        msg = message.text[10:]
        if msg == '':
            markup = types.ForceReply(selective=True)
            replymsg = bot.reply_to(message, 'What\'s the admin\'s ID?\n/cancel to stop the operation!', reply_markup=markup)
            bot.register_next_step_handler(replymsg, del_admin_step_id)
        
        elif msg.isdigit() == False:
            bot.reply_to(message, 'Ex. /deladmin 1234567')
            return
        
        elif msg.isdigit() and int(msg) in admin_users:
            bot.reply_to(message, 'Bye-bye admin!(´∩｀。)\n' + str(msg) + ' ' + admin_users[int(msg)])
            remove_key_dict(admin_users_file, admin_users, int(msg))

def del_admin_step_id(message):
    cid = get_user_id(message)
    id_to_del = message.text
    
    if id_to_del == '/cancel':
        return
    
    elif id_to_del.isdigit() and int(id_to_del) in admin_users:
        bot.reply_to(message, 'Bye-bye admin!(´∩｀。)\n' + str(id_to_del) + ' ' + admin_users[int(id_to_del)])
        remove_key_dict(admin_users_file, admin_users, int(id_to_del))

admin_commands['deladmin'] = 'Deletes admin by ID.'

@bot.message_handler(commands=['admins'])
def reply_admin_user_list(message):
    'Replies admin list'
    cid = get_user_id(message)
        
    if cid in admin_users:
        reply_text = 'My admins (/^▽^)/\n'
        reply_text += '==================\n'
        for key in admin_users:
            reply_text += '[' + str(key) + ']: ' + str(admin_users[key]) + '\n'
        reply_text += '=================='
        bot.reply_to(message, reply_text)
	
admin_commands['admins'] = 'List of all admins.'
