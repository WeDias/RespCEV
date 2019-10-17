import random
vitorias = 0
jogado = ''
while True:
    print('-' * 30)
    num = int(input('Digite Um Valor: '))
    jogador = ' '
    while jogador not in 'PI':
        jogador = str(input('[I]Impar\n[P]Par' + ' ' * 8)).strip().upper()
    pc = random.randint(1, 50)
    total = num + pc
    print(f'Você Escolheu {jogador} E O Numero {num}\nO PC Escolheu O Numero {pc}\nTotalizando {total}')
    if jogador == 'P' and total % 2 == 0:
        print('VOCÊ VENCEU!')
        vitorias += 1
    elif jogador == 'I' and total % 2 >= 1:
        print('VOCÊ VENCEU!')
        vitorias += 1
    else:
        if vitorias == 0:
            print('VOCÊ PERDEU!')
            print('-' * 30, '\nVOCÊ NÃO VENCEU UMA!')
        else:
            print('VOCÊ PERDEU!')
            print('-' * 30, f'\nVOCÊ VENCEU {vitorias} VEZES SEGUIDAS!')
        break
