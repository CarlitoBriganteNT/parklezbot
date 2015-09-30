'''
admin_module plugin for banning users.
(really unnecessary)
'''

from config import *

@bot.message_handler(commands=['ban'])
def reply_ban_user(message):
    cid = get_user_id(message)
        
    if cid in admin_users:
        msg = message.text[5:]

        if msg == '':
            bot.reply_to(message, 'Ex. /ban 1234567')
            return
        
        elif msg.isdigit() == False:
            bot.reply_to(message, 'Ex. /ban 1234567')
            return

        elif msg in regular_users:
            user_name = regular_users[msg]
        
        else:
            user_name = 'Unregistered banned guy!'

        if msg in admin_users:
            remove_key_dict('configs/admins.txt', admin_users, msg)
            
        add_key_dict('configs/banned.txt', banned_users, int(msg), user_name)
        bot.reply_to(message, 'Tchau ' + str(user_name) + '! (´∩｀。)')

admin_commands['ban'] = 'Bane usuário por ID.'

@bot.message_handler(commands=['unban'])
def reply_unban_user(message):
    cid = get_user_id(message)
        
    if str(cid) in admin_users:
        msg = message.text[7:]
        if msg == '':
            bot.reply_to(message, 'Ex. /unban 1234567')
            return
        
        elif msg.isdigit() == False:
            bot.reply_to(message, 'Ex. /unban 1234567')
            return
        
        elif msg.isdigit() and int(msg) in banned_users:
            bot.reply_to(message, 'Bem-vindo de volta!\nヽ(*⌒∇⌒*)ﾉ\n' + regular_users[msg])
            remove_key_dict('configs/banned.txt', banned_users, int(msg))
        else:
            bot.reply_to(message, 'Não tenho esse ID comigo!')

admin_commands['unban'] = 'Desbane usuário por ID.'
