import random
user = 0
pc = 1
tentativas = 0
while user != pc:
    user = int(input('\nDigite um Número de 0 a 10: '))
    pc = random.randint(0, 10)
    if user == pc:
        print('\nO Computador esolheu o Número {}\n\033[1;32mPARABENS! VOCÊ ACERTOU !\033[m'.format(pc))
        tentativas += 1
    else:
        print('\nO Computador escolheu o Número {}\n\033[1;31mVOCÊ PERDEU !\033[m'.format(pc))
        tentativas += 1
print('\nVocê Tentou {} Vezes Até Acertar!'.format(tentativas))
