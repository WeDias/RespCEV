from random import randint
from time import sleep
jogo = []
print('-' * 50)
num = int(input('Quantos Jogos Você Deseja: '))
print('-' * 50)
for c in range(num):
    t = 6
    while t > 0:
        t -= 1
        palpite = randint(1, 60)
        if palpite not in jogo:
            jogo.append(palpite)
        else:
            t += 1
    jogo.sort()
    sleep(0.25)
    print(f'Jogo {c + 1}: {jogo}')
    jogo.clear()
print('-' * 50)
