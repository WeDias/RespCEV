num = 0
resul = -999
rep = 's'
while rep == 's':
    if num < 999 or num > 999:
        num = int(input('Digite Um Numero: '))
        resul += num
        rep = 's'
    elif num == 999:
        rep = 'n'
print('A Soma Dos Numeros Digitados Foi: {}'.format(resul))
