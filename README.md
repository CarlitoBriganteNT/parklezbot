# parklezbot
Telegram bot made with PyTelegramBotAPI

**Requires Python 3 and [PyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) to run!**
#######################################
	Features:

 - Admin system. (with menus)
 - Subscriber system.
 - List handling.
 - .txt database system.
 - Lots of common functions to make life easier.
 - Tool to convert .wav to OPUS .ogg.
 - Easy drag and drop to enable/disable plugins.
 - Awesome plugins made by me and folks at the official pyTelegramBotAPI group.
 
#######################################
	Plugins:
	
 - Enabled by default:
	- admin_module.py (/admin, /addadmin /deladmin)
	- common_functions.py (no commands)
	- reply_help.py (/help)
	- reply_start.py (/start)
	- reply_stats.py (/stats)
	
 - Disabled:
	- admin_subscriber module.py (/post, /stop, /subscribe)
	- anime_module.py (/animes, /edit)
	- google_imgsearch.py (/img)
	- google_maps.py (/map)
	- happy_wheels module.py (/maps, /delmap)
	- jokes_module.py (/joke, /addjoke, /jokemenu or /settings)
	- linux_shell module.py (/shell)
	- listener_module.py (no commands, debug only)
	- reply_files ids.py (no commands, replies file's id's)
	- reply_rate.py (/rate)
	- reply_user id.py (/me)
	- sounds_module.py (/snds, /snd, /delsnd)
	
#######################################
	Bots using this base:
	
 - [@AndreasBOT](https://telegram.me/andreasbot) PORTUGUESE LANGUAGE!
 - [@IllegalJokesBOT](https://telegram.me/illegaljokesbot)
	
Write your token and set yourself as admin at config.py

I am releasing this bot 'as it is', I've translated everything I could.

**I strongly recommend you to read all the python files in the main and plugins folder.**

As you can see, I've separated all functions into modules just to make it easier to debug/enable/disable.** To enable a plugin, just drag it from the /disabled folder.**

All modules are globally loaded, and need config.py to know about the "bot" instance object of the telebot class, and also to have access to common_functions.py and global variables such as admin_users.

All extras included in this documentation folder are not supported anymore, they're just pieces of code I used somewhere in the project timeline.

anime module.py, happy wheels module.py and sounds module.py do not have any files for your enjoyment, since telegram only allow the file's owner to retrieve them! (telegram's behavior, long story.) So you have to send them to the bot yourself! (See /documentation/anime module/, before uploading videos!).

You can delete any .txt at any moment, since common_functions.py creates them when necessary! :)

In case you want to take any step further in this project, find me in telegram.** (I am not answering questions like: 'How can I send something to my subs?', 'How do I change the welcome message?')**

My telegram username: @parklez
www.telegram.me/parklez
