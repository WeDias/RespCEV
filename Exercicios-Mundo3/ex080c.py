from random import randint
from time import sleep
lista = list()
while True:
    for c in range(0, 5):
        num = randint(0, 9999)
        lista.append(num)
    sleep(0.25)
    lista.sort()
    print(f'{lista}')
    del lista[:]
