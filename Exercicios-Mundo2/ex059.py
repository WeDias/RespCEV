opc = 0
while not opc == 5:
    num1 = float(input('\nDigite O Primeiro Numero: '))
    num2 = float(input('Digite O Segundo Numero: '))
    print('\nO Que Você Deseja Fazer Agora: ')
    opc = int(input('[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR/MENOR\n[4]NOVOS NUMEROS\n[5]SAIR' + ' ' * 8))
    if opc == 1:
        print('\nA Soma Entre {} e {} é {}'.format(num1, num2, num1 + num2))
    elif opc == 2:
        print('\nA Multiplicação Entre {} e {} é {}'.format(num1, num2, num1 * num2))
    elif opc == 3:
        if num1 > num2:
            print('\nO Numero {} é Maior {}'.format(num1, num2))
        else:
            print('\nO Numero {} é Menor {}'.format(num1, num2))
print('Fim')
