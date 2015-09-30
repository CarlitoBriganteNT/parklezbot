def create_dict(file, dict_name=None):
    'Returns a new created file as dictionary.'
    if dict_name == None:
        dict_name = dict()
        
    with open(file, 'a') as f:
        f.write(str(dict_name))
    print(file, 'created!')
    
    return dict_name

def load_dict(file):
    'Returns a loaded file as a dictionary.'
    temp_dict = dict()
    try:
        with open(file, 'r', encoding='utf8') as f:
            temp_dict = eval(f.read())
        return temp_dict
    
    except FileNotFoundError:
        return create_dict(file)

def save_dict(file, dict_name):
    'Saves a dictionary into a file.'  
    try:
        with open(file, 'w', encoding='utf8') as f:
            f.write(str(dict_name))
            
    except FileNotFoundError:
        create_dict(file, dict_name)

def add_key_dict(file, dict_name, key, val):
    'Adds a key and a value to the memory and saves it into a file.'
    dict_name[key] = val
    save_dict(file, dict_name)

def remove_key_dict(file, dict_name, key):
    'Removes a key from the memory and saves it into a file.'
    try:
        del dict_name[key]
        save_dict(file, dict_name)
        
    except KeyError:
        print('Key', key, 'not found!')
        return

def print_dict(file):
    with open(file, 'r') as f:
        p_dict = eval(f.read())
    for key in sorted(p_dict.keys()):
        print(key, p_dict[key])

def file_input():
    arquivo = str(input('Nome do dicionário: '))

    if arquivo == '':
        exit()
    
    elif '.txt' not in arquivo:
        arquivo += '.txt'
        
    return arquivo

def main_menu():
    arquivo = file_input()
    counter = 0
    dicionario = load_dict(arquivo)
    keys_list = list(sorted(dicionario.keys()))
    print('=====================')
    for key in keys_list:
        print(counter, key, dicionario[key])
        counter += 1
    print('=====================')
    item = input('Escolha uma key: ')
    if item.isdigit():
        choosing = True
        while choosing:
            item = keys_list[int(item)]
            print('Item escolhido:', item)
            print('=====================')
            print('Escolha uma operação:')
            print('=====================')
            print('1. Deletar')
            print('2. Editar')
            print('3. Voltar')
            print('4. Sair')
            print('=====================')
            opcao = input('Opção: ')
            if opcao.isdigit():
                if opcao == '1':
                    remove_key_dict(arquivo, dicionario, item)
                    print('Key', item, 'removida com sucesso!')
                elif opcao == '2':
                    print('Qual valor devo atribuir a', item, '?')
                    valor = input('Valor: ')
                    add_key_dict(arquivo, dicionario, item, valor)
                    print('Valor:', valor, 'atribuído a', item, '!')
                elif opcao == '3':
                    main_menu()
                elif opcao == '4':
                    choosing = False
                    quit()
            else:
                main_menu()

main_menu()
