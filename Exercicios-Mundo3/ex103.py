def ficha(n, g):
    print('-=' * 20)
    print(f'O Jogador {n} Fez {g} Gols.')
    print('-=' * 20)


print('-=' * 20)
nome = str(input('Digite O Nome Do Jogador: '))
gols = input('Digite Os Gols: ')
if gols == '':
    gols = 0
if nome == '':
    nome = '<Desconhecido>'
ficha(nome, gols)