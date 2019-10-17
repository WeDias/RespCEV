import emoji
from random import choice
repetir = 1
print('-' * 50)
print(' '*15 + '\033[1;36mPEDRA, PAPEL, TESOURA\033[m')
while repetir == 1:
    print('-' * 50)
    jogador = int(input('\033[1;m[0]SAIR DO JOGO' + emoji.emojize(' :heavy_multiplication_x:') + '\n\n[1]PEDRA' + emoji.emojize(' :baseball:') + '\n[2]PAPEL' + emoji.emojize(' :page_facing_up:') + '\n[3]TESOURA\033[m' + emoji.emojize(' :scissors:')))
    opc = 'PEDRA', 'PAPEL', 'TESOURA'
    pc = choice(opc)
    if jogador == 0:
        repetir = 0
        print('\n' + ' ' * 10 + '\033[1;36mFIM DE JOGO OBRIGADO, POR JOGAR!\033[m')
    elif jogador == 1 and pc == 'TESOURA' or jogador == 2 and pc == 'PEDRA' or jogador == 3 and pc == 'PAPEL':
        print('\n\033[1mO PC Escolheu {} Portanto\033[m \033[1;32m[VOCÊ VENCEU!]\033[m'.format(pc))
    elif jogador == 1 and pc == 'PEDRA' or jogador == 2 and pc == 'PAPEL' or jogador == 3 and pc == 'TESOURA':
        print('\n\033[1mO PC Escolheu {} Portanto\033[m \033[1;33m[VOCÊS EMPATARAM!]\033[m'.format(pc))
    else:
        print('\n\033[1mO PC Escolheu {} Portanto\033[m \033[1;31m[VOCÊ PERDEU!]\033[m'.format(pc))
print('-' * 50)
