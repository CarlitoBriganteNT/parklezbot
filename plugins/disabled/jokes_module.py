'''
Reply a joke from 'database'
'''
import random

from config import *

users_settings = dict()
###############################
ra_file = 'files/jokes/racism.txt'
ra_jokes = load_dict(ra_file)

ss_file = 'files/jokes/sexandshit.txt'
ss_jokes = load_dict(ss_file)

re_file = 'files/jokes/religion.txt'
re_jokes = load_dict(re_file)

po_file = 'files/jokes/politics.txt'
po_jokes = load_dict(po_file)

cr_file = 'files/jokes/crime.txt'
cr_jokes = load_dict(cr_file)

se_file = 'files/jokes/sexism.txt'
se_jokes = load_dict(se_file)

il_file = 'files/jokes/illness.txt'
il_jokes = load_dict(il_file)

mo_file = 'files/jokes/mortality.txt'
mo_jokes = load_dict(mo_file)

tv_file = 'files/jokes/tv.txt'
tv_jokes = load_dict(tv_file)

ot_file = 'files/jokes/other.txt'
ot_jokes = load_dict(ot_file)
###############################
all_jokes = []

all_dicts = (ra_jokes, ss_jokes, re_jokes, po_jokes,
             cr_jokes, se_jokes, il_jokes, mo_jokes,
             tv_jokes, ot_jokes)

for category in all_dicts:
    for value in category.values():
        all_jokes.append(value)

### Core functionality ###
@bot.message_handler(commands=['joke'])
def reply_random_joke(message):
    cid = get_user_id(message)
    count_messages()
    if cid in users_steps:
        if users_steps[cid] == 'racism':
            bot.send_message(message.chat.id, random.choice(list(ra_jokes.values())))
        
        elif users_steps[cid] == 'sexandshit':
            bot.send_message(message.chat.id, random.choice(list(ss_jokes.values())))
                
        elif users_steps[cid] == 'religion':
            bot.send_message(message.chat.id, random.choice(list(re_jokes.values())))
                
        elif users_steps[cid] == 'politics':
            bot.send_message(message.chat.id, random.choice(list(po_jokes.values())))
                
        elif users_steps[cid] == 'crime':
            bot.send_message(message.chat.id, random.choice(list(cr_jokes.values())))
                
        elif users_steps[cid] == 'sexism':
            bot.send_message(message.chat.id, random.choice(list(se_jokes.values())))
                
        elif users_steps[cid] == 'illness':
            bot.send_message(message.chat.id, random.choice(list(il_jokes.values())))
                
        elif users_steps[cid] == 'mortality':
            bot.send_message(message.chat.id, random.choice(list(mo_jokes.values())))
                
        elif users_steps[cid] == 'tv':
            bot.send_message(message.chat.id, random.choice(list(tv_jokes.values())))
                
        elif users_steps[cid] == 'other':
            bot.send_message(message.chat.id, random.choice(list(ot_jokes.values())))
            
        else:
            bot.send_message(message.chat.id, random.choice(all_jokes))
    else:
        bot.send_message(message.chat.id, random.choice(all_jokes))
        
@bot.message_handler(commands=['jokemenu', 'settings'])
def reply_joke_menu(message):
    cid = get_user_id(message)
    users_steps[cid] = 'select_joke_type'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, selective=True)
    markup.row('Racism', 'Sex and Shit')
    markup.row('Religion', 'Politics')
    markup.row('Crime', 'Sexism')
    markup.row('Illness', 'Mortality')
    markup.row('TV', 'Other')
    markup.row('All categories!')
    bot.reply_to(message, 'Choose a joke category:', reply_markup=markup)
    
@bot.message_handler(func=lambda message: get_user_step(get_user_id(message)) == 'select_joke_type')
def select_joke_type(message):
    cid = get_user_id(message)
    option = message.text
    markup = types.ReplyKeyboardHide(selective=True)
    
    if option == 'Racism':
        users_steps[cid] = 'racism'
        bot.reply_to(message, 'Racism category selected!\nHit /joke to get it!', reply_markup=markup)

    elif option == 'Sex and Shit':
        users_steps[cid] = 'sexandshit'
        bot.reply_to(message, 'Sex and shit category selected!\nHit /joke to get it!', reply_markup=markup)

    elif option == 'Religion':
        users_steps[cid] = 'religion'
        bot.reply_to(message, 'Religion category selected!\nHit /joke to get it!', reply_markup=markup)
        
    elif option == 'Politics':
        users_steps[cid] = 'politics'
        bot.reply_to(message, 'Politics category selected!\nHit /joke to get it!', reply_markup=markup)
        
    elif option == 'Crime':
        users_steps[cid] = 'crime'
        bot.reply_to(message, 'Crime category selected!\nHit /joke to get it!', reply_markup=markup)
        
    elif option == 'Sexism':
        users_steps[cid] = 'sexism'
        bot.reply_to(message, 'Sexism category selected!\nHit /joke to get it!', reply_markup=markup)
        
    elif option == 'Illness':
        users_steps[cid] = 'illness'
        bot.reply_to(message, 'Illness category selected!\nHit /joke to get it!', reply_markup=markup)
        
    elif option == 'Mortality':
        users_steps[cid] = 'mortality'
        bot.reply_to(message, 'Mortality category selected!\nHit /joke to get it!', reply_markup=markup)
        
    elif option == 'TV':
        users_steps[cid] = 'tv'
        bot.reply_to(message, 'TV category selected!\nHit /joke to get it!', reply_markup=markup)
        
    elif option == 'Other':
        users_steps[cid] = 'other'
        bot.reply_to(message, 'Other category selected!\nHit /joke to get it!', reply_markup=markup)
        
    elif option == 'All categories!':
        users_steps[cid] = ''
        bot.reply_to(message, 'All categories selected!\nHit /joke to get it!', reply_markup=markup)

### File Manager ###
new_jokes = dict()
new_jokes_file = dict()

@bot.message_handler(func=lambda message: get_user_step(get_user_id(message)) == 'adding_new_jokes')
def receive_new_joke(message):
    cid = get_user_id(message)
    text = message.text
    print(text)
    if cid in admin_users and cid in new_jokes:
        if text.startswith('/'):
            bot.reply_to(message, 'I won\'t receive any more jokes!')
            users_steps[cid] = ''

        else:
            joke_dict = new_jokes[cid]
            joke_file = new_jokes_file[cid]
            list_len = len(list(joke_dict.keys())) + 1
            add_key_dict(joke_file, joke_dict, list_len, text)
            bot.send_message(message.chat.id, 'Joke added to: ' + str(joke_file))

@bot.message_handler(commands=['addjoke'])
def add_new_joke(message):
    cid = get_user_id(message)
    if cid in admin_users:
        markup = types.ForceReply(selective=True)
        text = 'Choose an option:\n\n'
        text += '/1 Racism\n'
        text += '/2 Sex and Shit\n'
        text += '/3 Religion\n'
        text += '/4 Politics\n'
        text += '/5 Crime\n'
        text += '/6 Sexism\n'
        text += '/7 Illness\n'
        text += '/8 Mortality\n'
        text += '/9 TV\n'
        text += '/10 Other\n'
        text += '\n/cancel'
        replymsg = bot.send_message(message.chat.id, text, reply_markup=markup)
        bot.register_next_step_handler(replymsg, choose_joke_category_step)

def choose_joke_category_step(message):
    cid = get_user_id(message)
    text = message.text
        
    if text == '/1':
        new_jokes[cid] = ra_jokes
        new_jokes_file[cid] = ra_file
        bot.reply_to(message, 'New jokes being added to ra_jokes!')

    elif text == '/2':
        new_jokes[cid] = ss_jokes
        new_jokes_file[cid] = ss_file
        bot.reply_to(message, 'New jokes being added to ss_jokes!')
        
    elif text == '/3':
        new_jokes[cid] = re_jokes
        new_jokes_file[cid] = re_file
        bot.reply_to(message, 'New jokes being added to re_jokes!')
        
    elif text == '/4':
        new_jokes[cid] = po_jokes
        new_jokes_file[cid] = po_file
        bot.reply_to(message, 'New jokes being added to po_jokes!')
        
    elif text == '/5':
        new_jokes[cid] = cr_jokes
        new_jokes_file[cid] = cr_file
        bot.reply_to(message, 'New jokes being added to cr_jokes!')
        
    elif text == '/6':
        new_jokes[cid] = se_jokes
        new_jokes_file[cid] = se_file
        bot.reply_to(message, 'New jokes being added to se_jokes!')
        
    elif text == '/7':
        new_jokes[cid] = il_jokes
        new_jokes_file[cid] = il_file
        bot.reply_to(message, 'New jokes being added to il_jokes!')
        
    elif text == '/8':
        new_jokes[cid] = mo_jokes
        new_jokes_file[cid] = mo_file
        bot.reply_to(message, 'New jokes being added to mo_jokes!')
        
    elif text == '/9':
        new_jokes[cid] = tv_jokes
        new_jokes_file[cid] = tv_file
        bot.reply_to(message, 'New jokes being added to tv_jokes!')
        
    elif text == '/10':
        new_jokes[cid] = ot_jokes
        new_jokes_file[cid] = ot_file
        bot.reply_to(message, 'New jokes being added to ot_jokes!')
    
    else:
        return
        
    users_steps[cid] = 'adding_new_jokes'
    
help_commands['joke'] = 'I throw a random joke.'
help_commands['jokemenu or /settings'] = 'Choose a joke category.'
admin_commands['addjoke'] = 'Adds a joke.'
