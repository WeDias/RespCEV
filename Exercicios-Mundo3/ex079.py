lista = list()
continuar = 'S'
print('-' * 35)
while continuar == 'S':
    num = int(input('Digite Um Numero: '))
    while num in lista:
        num = int(input('Numero Existente! Digite Outro: '))
    num = lista.append(num)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja Continuar[S/N]: ')).upper()
lista.sort()
print('-' * 35)
print('Você Digitou Os Seguintes Numeros:')
print(lista)
print('-' * 35)
