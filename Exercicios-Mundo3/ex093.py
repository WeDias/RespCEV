campeonato = dict()
gols = list()
print('-' * 50)
campeonato['nome'] = str(input('Nome Do Jogador: ')).capitalize()
partidas = int(input('Quantas Partidas Ele Jogou: '))
soma = 0
for c in range(partidas):
    gol = int(input(f'Quantos Gols Ele Fez Na {c +1}ª Partida: '))
    soma += gol
    gols.append(gol)
campeonato['gols'] = gols.copy()
campeonato['Total'] = soma
print('-' * 50)
print(campeonato)
print('-' * 50)
for k, v in campeonato.items():
    print(f'{k} = {v}')
print('-' * 50)
cont = 0
for i in campeonato['gols']:
    cont += 1
    print(f'Na {cont}ª Partida Ele Fez {i} Gols ')
print(f'O Jogador {campeonato["nome"]} Fez {campeonato["Total"]} Gols Em {cont} Partidas')
print('-' * 50)