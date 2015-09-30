'''
Module for listing admin commands in keyboard
Too much work and kinda unnecessary
'''

from config import *
from plugins.admin_module import *

@bot.message_handler(commands=['admin2'])
def reply_admin_keyboard(message):
    cid = get_user_id(message)

    if cid in admin_users:
        users_steps[cid] = 'select_admin_command'
        
        ############# This will create the keyboard based on admin_commands dictionary!
        cmd_list = sorted(list(admin_commands.keys()))
        tpl = 1
        row_width = 1
        tecla = []
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, selective=True, row_width=row_width)
        '''
        for key in cmd_list:
            tecla.append(key)
            if len(tecla) == tpl:
                markup.row(tecla[0], tecla[1])
                tecla = []
        '''
        for key in cmd_list:
            markup.row(key)
            
        markup.row('Fechar :3')
        ##############
        
        bot.send_message(cid, 'Os seguintes comandos estão disponíveis:', reply_markup=markup)

    else:
        bot.reply_to(message, 'Você não é um admin! \n(´∩｀。)')

#Message without "/" case
@bot.message_handler(func=lambda message: get_user_step(get_user_id(message)) == 'select_admin_command')
def select_admin_command(message):
    cid = message.chat.id
    msg = message.text

    if msg == 'addadmin':
        markup = types.ForceReply(selective=True)
        replymsg = bot.reply_to(message, 'Qual o ID do novo admin?', reply_markup=markup)
        bot.register_next_step_handler(replymsg, add_admin_step_id)
        users_steps[cid] = 0
        
    if msg == 'Fechar :3':
        markup = types.ReplyKeyboardHide(selective=True)
        bot.send_message(message.chat.id, 'Pronto!', reply_markup=markup)
        users_steps[cid] = 0
        
    if msg == 'deladmin':
        markup = types.ForceReply(selective=True)
        replymsg = bot.reply_to(message, 'Qual o ID do admin?', reply_markup=markup)
        bot.register_next_step_handler(replymsg, del_admin_step_id)
        users_steps[cid] = 0
        
    if msg == 'admins':
        reply_admin_user_list(message)
        users_steps[cid] = 0
        
#Message with "/" case
@bot.message_handler(commands=['hide'])
def reply_hide_keyboard(message):
    markup = types.ReplyKeyboardHide(selective=True)
    bot.send_message(message.chat.id, 'Pronto!', reply_markup=markup)
