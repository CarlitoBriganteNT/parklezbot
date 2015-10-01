from config import *

animes_list_file = 'files/animes.txt'
animes_list = load_dict(animes_list_file)

anime_choice = dict()
new_anime_id = dict()
new_anime_name = dict()

### Anime listing ###
@bot.message_handler(commands=['animes'])
def reply_anime_list(message):
    cid = get_user_id(message)
    
    if cid in users_steps and users_steps[cid] == 'edit_mode':
        markup = types.ForceReply(selective=True)
        msg = bot.reply_to(message, 'What serie whould I edit?', reply_markup=markup)

        bot.register_next_step_handler(msg, editor_get_anime_id)
    else:
        users_steps[cid] = 'reply_anime_info_and_episodes'
    
    page_input = message.text[8:]
    
    if page_input.isdigit():
        page = int(page_input)
    else:
        page = 0

    ipp = 20 #items per page
    start = ipp * page
    end = start + ipp

    anime_list = sorted(list(animes_list.keys()))
    list_len = len(anime_list)
    
    #Check if there is enough elements to fill.
    if list_len - start < ipp:
        keys = int(list_len - start)
    else:
        keys = int(ipp)
        
    counter = 0

    reply_msg = 'Available Series:\n'
    reply_msg += '==================\n'
    for key in range(keys):
        reply_msg += '/' + str(start+counter) + '. ' + anime_list[(start+key)] + '\n'
        counter += 1
    reply_msg += '=================='
    reply_msg += '\nTap the desired number.'
    if int(list_len/ipp) > page and page > 0:
        #reply_msg += '\nPágina nº' + str(page) + ' de ' + str(int(list_len/ipp)) + '.'
        reply_msg += '\nNext page. = /animes' + str(page+1)
    reply_msg += '\n/close to exit.'
    bot.send_message(message.chat.id, reply_msg)

help_commands['animes'] = 'List of subbed anime (pt-br)!'

@bot.message_handler(func=lambda message: get_user_step(get_user_id(message)) == 'reply_anime_info_and_episodes')
def reply_anime_info_and_episodes(message):
    cid = get_user_id(message)
    
    users_steps[cid] = 'reply_anime_episode_download'
    
    anime_id = message.text[1:]

    if '@AndreasBOT' in anime_id:
        anime_id = anime_id.strip('@AndreasBOT')

    anime_list = sorted(list(animes_list.keys()))
        
    if anime_id.isdigit() and int(anime_id)+1 <= len(anime_list):

        anime_file = animes_list[anime_list[int(anime_id)]]

        anime_choice[cid] = anime_file #Hold the chosen file for the next step!
        
        anime_dict = load_dict(str(anime_file))
        
        bot.send_photo(message.chat.id, anime_dict['Poster'])
        
        episode_list = list() #The following lines will convert strings to numbers, so that a list with 12 itens, don't show up as 1,11,12,2,3,4...
        
        for episode in anime_dict.keys():
            if episode.isdigit():
                episode_list.append(int(episode))

        reply_msg = '======Description======\n'
        reply_msg += anime_dict['Description'] + '\n'
        reply_msg += '=======Genre=======\n'
        reply_msg += anime_dict['Genre'] + '\n'
        reply_msg += '====Availability====\n'
        for episode in sorted(episode_list):
            reply_msg += 'Episode: /' + str(episode) + '\n'
        reply_msg += '====================\n'
        reply_msg += 'Tap the desired number.\n'
        reply_msg += 'Return to list: /animes or /close to exit.'
        bot.send_message(message.chat.id, reply_msg)

    else:
        users_steps[cid] = 0
        bot.reply_to(message, 'Anime menu deactivated!')

@bot.message_handler(func=lambda message: get_user_step(get_user_id(message)) == 'reply_anime_episode_download')
def reply_anime_episode_download(message):
    cid = get_user_id(message)
    
    anime_id = message.text[1:]
    
    if '@AndreasBOT' in anime_id:
        anime_id = anime_id.strip('@AndreasBOT')

    anime_dict = load_dict(anime_choice[cid])
        
    if anime_id.isdigit() and int(anime_id) <= len(anime_dict)-3:
        if anime_id in anime_dict:
            bot.send_document(message.chat.id, anime_dict[anime_id])

    else:
        users_steps[cid] = 0
        bot.reply_to(message, 'Anime menu deactivated!')

### Anime editor ###
@bot.message_handler(commands=['edit'])
def reply_anime_editor(message):
    cid = get_user_id(message)
    if cid in admin_users:
        users_steps[cid] = 'edit_mode'
        reply_anime_list(message)

def editor_get_anime_id(message):
    cid = get_user_id(message)
    
    anime_id = message.text[1:]
    
    anime_list = sorted(list(animes_list.keys()))
    
    if anime_id.isdigit() and int(anime_id)+1 <= len(anime_list):
        anime_file = animes_list[anime_list[int(anime_id)]]

        anime_choice[cid] = anime_file #Hold the chosen file for the next step!
        
        bot.reply_to(message, 'Send-me the poster!')
        
        users_steps[cid] = 'editor_get_poster'
        
    else:
        bot.reply_to(message, 'Operation canceled!')
        users_steps[cid] = 0
        
@bot.message_handler(func=lambda message: get_user_step(get_user_id(message)) == 'editor_get_poster', content_types=['photo'])
def editor_get_poster(message):
    cid = get_user_id(message)
    
    if cid in users_steps and users_steps[cid] == 'editor_get_poster':
        
        anime_dict = load_dict(anime_choice[cid])
        anime_dict['Poster'] = message.photo[-1].file_id
        save_dict(anime_choice[cid], anime_dict)

        markup = types.ForceReply(selective=True)
        msg = bot.reply_to(message, 'Now, send me the serie\'s description.', reply_markup=markup)
        users_steps[cid] = ''
        bot.register_next_step_handler(msg, editor_anime_description)
        
def editor_anime_description(message):
    cid = get_user_id(message)
    
    text = message.text
    
    if text == '/cancel':
        bot.reply_to(message, 'Operation canceled!')
        users_steps[cid] = 0
        return
    
    anime_dict = load_dict(anime_choice[cid])
    anime_dict['Description'] = text
    save_dict(anime_choice[cid], anime_dict)
    
    markup = types.ForceReply(selective=True)
    msg = bot.reply_to(message, 'At last, tell me the genre.', reply_markup=markup)
    
    bot.register_next_step_handler(msg, editor_anime_genre)
    
def editor_anime_genre(message):
    cid = get_user_id(message)
    
    text = message.text
    
    if text == '/cancel':
        bot.reply_to(message, 'Operation canceled!')
        users_steps[cid] = 0
        return
    
    anime_dict = load_dict(anime_choice[cid])
    anime_dict['Genre'] = text
    
    save_dict(anime_choice[cid], anime_dict)
    
    bot.send_message(message.chat.id, 'Everything edited and saved!\n(/^▽^)/')

admin_commands['edit'] = 'Opens the edit mode for anime series.'

### File Manager ###
@bot.message_handler(func=lambda message: get_file_extention(message) == '.mp4', content_types=['document'])
def receive_new_anime_episode(message):
    cid = get_user_id(message)
    
    file_name, extension = message.document.file_name.split('.')

    if extension == 'mp4' and cid in admin_users:
        new_anime_id[cid] = message.document.file_id
        is_in_format, name, episode = check_file_name_format(file_name)
        
        if is_in_format:
            if name in animes_list:
                new_anime_ep = load_dict('files/animes/' + str(name) + '.txt')
                add_key_dict('files/animes/' + str(name) + '.txt', new_anime_ep, episode, new_anime_id[cid])
                bot.reply_to(message, 'Serie exists, episode re(added).')
                
            else:
                new_anime_ep = create_new_anime_dict(name)
                add_key_dict('files/animes/' + str(name) + '.txt', new_anime_ep, episode, new_anime_id[cid])
                bot.reply_to(message, 'New serie! first episode added!')
        else:
            markup = types.ForceReply(selective=True)
            msg = bot.reply_to(message, 'What is the serie\'s name?\nWrite how it will be listed!\n/cancel to stop the operation!', reply_markup=markup)

            bot.register_next_step_handler(msg, choose_anime_name)

def create_new_anime_dict(anime_name):
    new_path = 'files/animes/' + str(anime_name) + '.txt'
    add_key_dict(animes_list_file, animes_list, anime_name, new_path)

    new_dict = create_dict(new_path)
    new_dict['Poster'] = 'AgADAQADmbExGzCXsAFoBUIdRnssuIEE2ykABEp6LoW_dAvwHPwAAgI'
    new_dict['Description'] = 'Nothing yet.'
    new_dict['Genre'] = 'None yet.'
    save_dict(new_path, new_dict)
    return new_dict
    
def check_file_name_format(file_name):
    if file_name[-1] == ')' and file_name.find(' ('):
        start = file_name.find('(') + 1
        end = len(file_name) - 1
        name = file_name[:start-2]
        
        if file_name[start:end].isdigit():
            return True, name, file_name[start:end]

    else:
        return False, 0, 0
    
def choose_anime_name(message):
    cid = get_user_id(message)
    
    name = message.text
    new_anime_name[cid] = name

    markup = types.ForceReply(selective=True)
        
    if name == '/cancel':
        bot.reply_to(message, 'Operation canceled!')
        return
        
    elif name in animes_list:
        msg = bot.reply_to(message, 'Serie exists! What episode should I link it?', reply_markup=markup)
        bot.register_next_step_handler(msg, choose_anime_episode)
    
    else:
        create_new_anime_dict(name)
        msg = bot.reply_to(message, 'New serie! What episode should I link it?', reply_markup=markup)
        bot.register_next_step_handler(msg, choose_anime_episode)

def choose_anime_episode(message):
    cid = get_user_id(message)
    episode = message.text

    if episode.isdigit():
        new_anime_ep = load_dict('files/animes/' + str(new_anime_name[cid]) + '.txt')
        add_key_dict('files/animes/' + str(new_anime_name[cid]) + '.txt', new_anime_ep, episode, new_anime_id[cid])
        bot.reply_to(message, 'Anime (now) exists and episode has been (re)added!')

    else:
        bot.reply_to(message, 'Operation canceled!')
        return