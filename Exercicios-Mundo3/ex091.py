from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador 1': randint(1, 12),
        'jogador 2': randint(1, 12),
        'jogador 3': randint(1, 12),
        'jogador 4': randint(1, 12)}
rank = list()
for k, v in jogo.items():
    sleep(1)
    print(k, f'Tirou {v} Nos Dados')
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
sleep(1)
print()
for i, v in enumerate(rank):
    print(f'{i +1}º Lugar: {v[0]} com {v[1]}')