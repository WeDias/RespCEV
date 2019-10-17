todos = list()
pessoa = list()
nleve = list()
npesado = list()
continuar = 'S'
pesado = leve = 0
while continuar == 'S':
    nome = str(input('Digite O Nome: ').upper())
    pessoa.append(nome)
    peso = int(input('Digite Seu Peso: '))
    if pesado == 0:
        pesado = peso
        leve = peso
    elif peso > pesado:
        pesado = peso
    elif peso < leve:
        leve = peso
    pessoa.append(peso)
    todos.append(pessoa[:])
    pessoa.clear()
    continuar = str(input('DESEJA CONTINUAR[S/N]: ')).upper()
c = -1
for carac in todos:
    c += 1
    if carac[:][1] == pesado:
        npesado.append(todos[c][0])
    if carac[:][1] == leve:
        nleve.append(todos[c][0])
print('-' * 50)
print(f'\n{todos}')
print(f'\nForam Cadastrados {len(todos)} Pessoas')
print(f'O Mais Pesado Foi {npesado} Com {pesado} KG E O Menos Pesado Foi {nleve} Com {leve} KG')
