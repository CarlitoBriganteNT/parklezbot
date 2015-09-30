'''
Module to reply things IDs.

The line:
    (func=lambda message: True, ...)
seems to be unnecessary for replying file id at any circunstance.
'''

from config import *

#audio:
@bot.message_handler(func=lambda message: True, content_types=['audio'])
def get_audio_id(message):
    bot.reply_to(message, 'Your audio ID is: ' + message.audio.file_id)

#voice:
@bot.message_handler(func=lambda message: True, content_types=['voice'])
def get_voice_id(message):
    bot.reply_to(message, 'Your voice ID is: ' + message.voice.file_id)

#document:
@bot.message_handler(func=lambda message: True, content_types=['document'])
def get_doc_id(message):
    bot.reply_to(message, 'Your document ID is: ' + message.document.file_id
                 + '\n' + message.document.file_name)
    
#photo:
@bot.message_handler(func=lambda message: True, content_types=['photo'])
def get_pic_id(message):
    bot.reply_to(message, 'Your photo ID is: ' + message.photo[-1].file_id)

#sticker:
@bot.message_handler(func=lambda message: True, content_types=['sticker'])
def get_sticker_id(message):
    bot.reply_to(message, 'Your sticker ID is: ' + message.sticker.file_id)

#video:
@bot.message_handler(func=lambda message: True, content_types=['video'])
def get_video_id(message):
    bot.reply_to(message, 'Your video ID is: ' + message.video.file_id)
