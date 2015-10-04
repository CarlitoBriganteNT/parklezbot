'''
Python console, it's not an actual IDLE but... it's powerful.
I don't know how to catch erros like syntax error instead of blank messages...

I could not use this InteractiveConsole instance
to work within the bot's globals() and locals(). (is there a way?)
'''

from code import InteractiveConsole
import sys

class OutputCache:
    'Cache the stdout text so we can analyze it before returning it'
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.out = []
        
    def write(self, line):
        self.out.append(line)
        
    def flush(self):
        output = '\n'.join(self.out)
        self.reset()
        return output

class Console(InteractiveConsole):
    'Wrapper around Python that can receive lines of code'
    def __init__(self):
        self.stdout = sys.stdout
        self.cache = OutputCache()
        InteractiveConsole.__init__(self)

    def get_output(self):
        sys.stdout = self.cache
        
    def return_output(self):
        sys.stdout = self.stdout

    def push(self, line):
        'Sends code to the console'
        self.get_output()
        
        InteractiveConsole.push(self, line)
        
        self.return_output()
        
        output = self.cache.flush()
        
        return output

bot_console = Console()

from config import *

@bot.message_handler(commands=['python'])
def reply_python_code(message):
    cid = get_user_id(message)
    users_steps[cid] = 'python'

    if cid in admin_users:
        bot.send_message(message.chat.id, 'You\'re in Python 3 console mode.\nUse /cancel to exit.')
        #markup = types.ForceReply(selective=False)
        #msg = bot.send_message(message.chat.id, 'Write your python 3 code:', reply_markup=markup)
        #bot.register_next_step_handler(msg, run_code)

@bot.message_handler(func=lambda message: get_user_step(get_user_id(message)) == 'python')
def run_code(message):
    cid = get_user_id(message)
    code_line = message.text
    
    if code_line.startswith('/'):
        users_steps[cid] = ''
        bot.reply_to(message, 'Python mode deactivated!')
        return
    
    result = str(bot_console.push(message.text))
    
    if result == '':
        bot.send_message(message.chat.id, 'Blank result.')
    else:
        bot.send_message(message.chat.id, result)

admin_commands['python'] = '[BETA] Enters in a clean python 3 console.'
