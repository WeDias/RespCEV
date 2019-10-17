lista = list()
print('digite -1 para sair')
while True:
    num = int(input('Digite Um Numero: '))
    if num != - 1:
        lista.append(num)
    else:
        break
lista.sort(reverse=True)
print('-' * 50)
print(lista)
print('-' * 50)
print(f'Você Digitou {len(lista)} Numeros')
if 5 in lista:
    print('O 5 Foi Digitado')
else:
    print('O Valor 5 Não Foi Digitado')
print('-' * 50)
