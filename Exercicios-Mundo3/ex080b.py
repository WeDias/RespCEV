from random import randint
from time import sleep
lista = list()
while True:
    for c in range(0, 5):
        num = randint(0, 100)
        if c == 0 or num > lista[-1]:
            lista.append(num)
        else:
            pos = 0
            while pos < len(lista):
                if num <= lista[pos]:
                    lista.insert(pos, num)
                    break
                pos += 1
    sleep(0)
    print(f'\033[32m{lista}')
    del lista[:]
