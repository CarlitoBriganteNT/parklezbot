# parklezbot
Telegram bot made with PyTelegramBotAPI

#######################################
	Features:

 - Admin system.
 - Subscriber system.
 - List handling.
 - .txt database system.
 - Lots of common functions to make life easier.
 - Awesome plugins made by me and folks at the official pyTelegramBotAPI group.

#######################################

TESTED ON PYTHON 3 ONLY!!!

Write your token at config.py

I am releasing this bot 'as it is', I've translated everything I could.

I strongly recommend you to read all the python files not in this documentation folder, but in the main and plugins folder.

As you can see, I've separated all functions into modules just to make it easier to debug/enable/disable.

All modules are globally loaded, and need config.py to know about the "bot" instance object of the telebot class, and also to have access to common_functions.py and global variables such as admin_users.

All extras included in this documentation folder are not supported anymore, they're just pieces of code I used somewhere in the project timeline.

anime_module.py may be a little complicated, so I brought some explaination
in anime module folder.

You can deleted all the .txt files in case you want to do so. Common_functions.py will re-create it if needed by any plugin.

In case you want to take any step further in this project, find me in telegram. (I am not answering questions like: 'How can I send something to my subs?')

My telegram username: @parklez