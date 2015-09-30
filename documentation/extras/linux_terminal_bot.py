# -*- coding: utf-8 -*-
 
import telebot
from telebot import types
import time
import subprocess
 
 
TOKEN = "your token"
 
bot = telebot.TeleBot(TOKEN)
 
def listener(messages):
    """
   When new messages arrive TeleBot will call this function.
   """
    for m in messages:
        if m.content_type == 'text' and m.from_user.id == yourID:
            # print the sent message to the console
            print str(m.from_user.first_name) + " [" + str(m.chat.id) + "]: " + m.text
            execute_command(m)
 
bot.set_update_listener(listener)
 
 
def execute_command(message):
    cid = message.chat.id
    result_command = subprocess.Popen(message.text, shell=True, stdout=subprocess.PIPE).stdout.read()
    try:
        bot.send_message( cid, result_command)
    except:
        exception = True
    else:
        exception = False
   
    if exception:
        if result_command == "":
            bot.send_message( cid, "Empty output")
        else:
            f = open( 'tmp.txt', 'w')
            f.write( result_command)
            f.close()
            bot.send_document( cid, open( 'tmp.txt', 'rb'))
 
 
bot.polling(none_stop=True)
