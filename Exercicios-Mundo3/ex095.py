time = list()
jogador = dict()
gols = list()
while True:
    print('-' * 50)
    jogador['nome'] = str(input('Nome Do Jogador: ')).capitalize()
    partidas = int(input('Quantas Partidas Ele Jogou: '))
    soma = 0
    for c in range(partidas):
        gol = int(input(f'Quantos Gols Ele Fez Na {c +1}ª Partida: '))
        soma += gol
        gols.append(gol)
    jogador['gols'] = gols.copy()
    jogador['Total'] = soma
    time.append(jogador.copy())
    gols.clear()
    while True:
        continuar = str(input('Deseja Continuar[S/N]: ')).upper()
        if continuar not in 'SN':
            print('ERRO DIGITE S OU N !')
        elif continuar == 'S':
            break
        else:
            break
    if continuar == 'N':
        break
print('-' * 50)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 50)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 50)
while True:
    busca = int(input('Mostrar Dados De Qual Jogadoe: (999 Para Parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print('ERRO JOGADOR NÂO EXISTE !')
    else:
        print(f'Dados Do Jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'No Jogo {i +1} Fez {g} Gols')
    print('-' * 50)
