from random import randint
lista = list()
pares = list()
impares = list()
print('[0]RANDON\n[-1]SAIR\n')
while True:
    num = int(input('Digite Um Numero: '))
    if num > 0:
        lista.append(num)
        if 0 == num % 2 and num != 0:
            pares.append(num)
        elif 0 != num % 2 > 0:
            impares.append(num)
    elif num == 0:
        repetir = int(input('Quantos Numeros Deseja: '))
        for rep in range(0, repetir):
            rep = randint(1, 999)
            lista.append(rep)
            if 0 == rep % 2 and rep != 0:
                pares.append(rep)
            elif 0 != rep % 2 > 0:
                impares.append(rep)
    else:
        break
print('-' * 50)
lista.sort()
print(f'Você Digitou:\n{lista}')
print('-' * 50)
pares.sort()
print(f'Os Numeros Pares Foram:\n{pares}')
print('-' * 50)
impares.sort()
print(f'Os Numeros Impares Foram:\n{impares}')
print('-' * 50)
