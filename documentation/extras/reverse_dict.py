value_to_find = ''
if value_to_find == '':
    #bot.reply_to(message, 'Exemplo: /getid @fulano')
    print('You haven\'t written anything.')
elif value_to_find in regular_users.values():
    for key, value in regular_users.items():
        if value_to_find == value:
            value_to_find = key
            #bot.reply_to(message, 'ID: ' + str(key))
            print(key)
else:
    #bot.reply_to(message, 'Não achei! :C')
    print('Coudn\'t find!')
