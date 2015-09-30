import json
import urllib.request, urllib.error, urllib.parse
import random

from config import *

@bot.message_handler(commands=['img'])
def command_img(message):
    img_to_find = message.text[5:]
    
    if img_to_find == '':
        bot.reply_to(message, 'Ex. /img test')
        return
        
    elif ' ' in img_to_find:
        img_to_find = img_to_find.replace(' ', '+')
        
    try:
        img_to_find.encode('utf-8')
        link = urllib.request.urlopen("https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + img_to_find)
        data = json.loads(link.read().decode('utf8'))
        rnd_no = random.randrange(0, 4)
        image = urllib.request.URLopener()
        image.retrieve(data['responseData']['results'][rnd_no]['unescapedUrl'], "files/tmp.jpg")
        bot.send_photo(message.chat.id, open( 'files/tmp.jpg', 'rb'))
    except (UnicodeEncodeError, IndexError, urllib.error.HTTPError):
        pass
    
help_commands['img'] = 'Search for a google image.'
