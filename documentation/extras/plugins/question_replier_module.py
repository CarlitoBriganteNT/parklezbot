'''
Reply with random answers uppon some circunstances.
However, it's really faulty since "in" isn't precise enough.
'''
import random

from config import *

help_text = 'Como perguntar:\n/perg é verdade?\n/perg quando choverá?\n/perg fulano é gay?'

@bot.message_handler(commands=['perg'])
def reply_answer_question_mark(message):
    mt = message.text
    
    if mt[6:] == '':
        bot.reply_to(message, help_text)

    elif mt[6:] == 'AndreasBOT':
        bot.reply_to(message, help_text)

    #Zarok(c)
        '''
    elif 'onde' in mt and '?' in mt:
        bot.reply_to(message, get_random_local_answer())

    elif 'ou' in mt and '?' in mt:
        things = []
        mt = mt.strip('/perg ')
        mt = mt.strip('?')
        for x in mt.split(' ou '):
            things.append(x)
        prefference = random.sample(things, 1)
        prefference = 'Eu prefiro ' + str(prefference).strip("['']") + '.'
        bot.reply_to(message, prefference)
        '''
            
    elif 'quando' in mt and '?' in mt:
        bot.reply_to(message, get_random_time_answer())
        
    elif 'gay' in mt and '?' in mt:
        bot.reply_to(message, get_random_gay_answer())
        
    elif '?' in mt:
        bot.reply_to(message, get_random_answer())

help_commands['ask with "?"'] = 'I answer some of your deep questions.'

def get_random_local_answer():
    respostas = ['Na puta que pariu!', 'Na casa do caralho!',
                 'Na esquina.', 'No barriu do chaves.',
                 'Na peida.', 'Aqui perto.', 'Na terra do Shrek, em Tão, tão distante.',
                 'Na de_dust2.', 'Na fenda do biquini.', 'No teu cu. D:',
                 'Na tua casa.', 'Na igreja mais próxima.', 'No putero mais próximo.',
                 'Lá depois do cu do judas.']
    return random.sample(respostas, 1)

def get_random_time_answer():
    respostas = ['Em breve.', 'No dia de São Nunca...',
                 'Mais tempo do que imaginas...', 'Antes tarde do que nunca.'
                 'Amanhã', 'Daqui a duas horas.', 'Na próxima sexta feira 13.',
                 'Na próxima lua cheia.', 'Quando deus quiser.',
                 'Quando menos imaginar...', '29 de Fevereiro.', 'Ano que vem.',
                 'Nunca, nunquinha, jamais!']
    return random.sample(respostas, 1)

def get_random_answer():
    respostas = ['Sim ヽ(*⌒∇⌒*)ﾉ', 'Não（ ＴДＴ）',
                 'Talvez （＾～＾）', 'Não sei... ヽ（´ー｀）┌',
                 'Mas é claro (*^▽^*)', 'Não mesmo! (´∩｀。)' ]
    return random.sample(respostas, 1)

def get_random_gay_answer():
    respostas = ['Gay e orgulhoso ainda!', 'Gay? Jamais!',
                 'Tão gay quanto o Elton John!', 'Claro que não!',
                 'Gay ardente e oscioso!', 'Nem.']
    return random.sample(respostas, 1)
