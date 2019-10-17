todos = list()
pessoa = dict()
print('-' * 50)
cadastrados = mulheres = media = 0
while True:
    cadastrados += 1
    nome = str(input('Digite O Nome: ')).capitalize()
    while True:
        sexo = str(input('Digite Seu Sexo[M/F]: ')).upper()
        if sexo not in 'MF':
            print('\033[31mERRO DIGITE M OU F !\033[m')
        else:
            if sexo == 'F':
                mulheres += 1
                break
            break
    while True:
        idade = int(input('Digite A Idade: '))
        media += idade
        if idade not in range(1, 150):
            print('\033[31mERRO DIGITE UMA IDADE VALIDA !\033[m')
        else:
            break
    pessoa['nome'] = nome
    pessoa['sexo'] = sexo
    pessoa['idade'] = idade
    todos.append(pessoa.copy())
    while True:
        print('-' * 50)
        continuar = str(input('Deseja Continuar[S/N]: ')).upper()
        if continuar not in 'SN':
            print('\033[31mERRO DIGITE S OU N !\033[m')
        else:
            print('-' * 50)
            break
    if continuar == 'N':
        break
print(f'Foram Cadastrados {cadastrados} Pessoas.')
print(f'Foram Cadastradas {mulheres} Mulheres:', end=' ')
for p in todos:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=', ')
print()
print(f'A Media De Idade Foi {media / cadastrados:.2f} Anos.')
print('-' * 50)
print('Os Maiores Que A Media São:')
for p in todos:
    if p['idade'] > media / cadastrados:
        print(end='')
        for k, v in p.items():
            print(f'{k} {v}', end=' ')
        print()
print('-' * 50)
