num1 = int(input('Digite Um Numero Inteiro: '))
print('''Escolha Uma Das Bases Para Conversão
[1]CONVERTER PARA BINÁRIO
[2]CONVERTER PARA OCTTAL
[3]CONVERTER PARA HEXADECIMAL''')
opcao = int(input('Sua Opcção: '))
if opcao == 1:
    print('{} Convertido para Binário é: {}'.format(num1, bin(num1)[2:]))
elif opcao == 2:
    print('{} Convertido para Octal é: {}'.format(num1, oct(num1)[2:]))
elif opcao == 3:
    print('{} Convertido para Hexadecimal é: {}'.format(num1, hex(num1)[2:]))
else:
    print('Opção Invalida Tente Novamente!')
