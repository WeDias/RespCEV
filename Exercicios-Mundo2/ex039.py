import datetime
ano = int(input('\033[1;34mDigite O \033[m\033[1mAno\033[m\033[1;34m em Que Você Nasceu:\033[m '))
opc = str(input('\033[1;34mVocê Já Se Alistou:\033[m[S/N]')).lower()
idade = int(datetime.date.today().year) - ano
if idade == 18 and opc == 'n':
    print('\n\033[1;34mVocê Deve Se Alistar Este Ano')
elif idade < 18:
    if  idade < 17:
        print('\n\033[1;32mFaltam {} Anos Para Você Se Alistar!\033[m'.format(18 - idade))
    elif idade == 17:
        print('\n\033[1;32mFalta 1 Ano Para Você Se Alistar\033[m')
elif idade > 18 and opc == 's':
    if idade == 19:
        print('\n\033[1;31mVocê Se Alistou Há 1 Ano\033[m')
    elif idade > 19:
        print('\n\033[1;31mVocê Se Alistou Há {} Anos\033[m'.format(idade - 18))
elif idade > 18 and opc == 'n':
    if idade == 19:
        print('\n\033[1;31mVocê Não Se Alistou Há 1 Ano\033[m')
    elif idade > 19:
        print('\n\033[1;31mVocê Não Se Alistou Há {} Anos\033[m'.format(idade - 18))
elif idade == 18 and opc == 's':
    print('\033[1;34m-\033[m' * 36)
    print('\033[1;34mAGUARDE A CONVOCAÇÃO DA\033[m AERONAUTICA!')
    print('\033[1;34m-\033[m' * 36)
