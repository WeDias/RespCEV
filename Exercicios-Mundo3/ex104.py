def leiaint():
    while True:
        n = input('Digite Um Numero: ')
        if n.isnumeric():
            break
        else:
            print('\033[31mERRO: Digite Um Numero!\033[m')
    print(f'Você Digitou {n}')


leiaint()