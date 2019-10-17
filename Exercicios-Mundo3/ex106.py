def ajuda():
    while True:
        txt = input('\033[1;46mDigite O Comando Que Você Tem Duvida: ')
        if txt not in 'FIMfim':
            print(f'Ajuda Para O Comando: \033[1;34;40m{txt:^16}\033[m')
            print('\033[1;34;40m', end='')
            print('-=' * 50)
            help(txt)
            print('\033[m')
        elif txt in 'FIMfim':
            print(f'\033[1;34;40m{txt:^38}\033[m')
            break


ajuda()
