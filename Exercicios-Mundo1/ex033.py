num1 = int(input('Digite um Numero: '))
num2 = int(input('Digite um Numero: '))
num3 = int(input('Digite um Numero: '))

if num1 > num2 and num1 > num3:
    print('O Numero {} É O maior'.format(num1))
if num2 > num1 and num2 > num3:
    print('O Numero {} É O Maior'.format(num2))
if num3 > num1 and num3 > num2:
    print('O Numero {} É O Maior'.format(num3))

if num1 < num2 and num1 < num3:
    print('O Numero {} É O menor'.format(num1))
if num2 < num1 and num2 < num3:
    print('O Numero {} É O Menor'.format(num2))
if num3 < num1 and num3 < num2:
    print('O Numero {} É O Menor'.format(num3))
