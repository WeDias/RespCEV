num1 = int(input('Digite Um Numero: '))
tot = 0
for contador in range(1, num1 + 1):
    if num1 % contador == 0:
        print('\033[34m', end=' ')
        tot = tot + 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(contador), end=' ')
if tot == 2:
    print(' \nÉ UM NÚMERO PRIMO')
else:
    print(' \nNÃO É UM NUMERO PRIMO')
