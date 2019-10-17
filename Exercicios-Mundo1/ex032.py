ano = int(input('Digite o Ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O Ano É Bissexto!')
else:
    print('O Ano Não É Bissexto')