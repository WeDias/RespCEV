def sorteia():
    from random import randint
    from time import sleep
    sleep(0.5)
    print(f'Sorteando: ', end=' ')
    for n in range(5):
        n = randint(1, 100)
        sleep(0.5)
        print(f'{n}', end=', ')
        numeros.append(n)
    print()
    sleep(0.5)


def somapar():
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f'A Soma Dos Pares É: {soma}')


numeros = list()
sorteia()
somapar()