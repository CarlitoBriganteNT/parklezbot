def print_dict(file):
    with open(file, 'r') as f:
        p_dict = eval(f.read())
    for key in sorted(p_dict.keys()):
        print(key, p_dict[key])

running = True
while running:
    arquivo = str(input('Nome do dicionário: '))

    if arquivo == '':
        running = False
    
    elif '.txt' not in arquivo:
        arquivo += '.txt'

    if running:
        print_dict(arquivo)
