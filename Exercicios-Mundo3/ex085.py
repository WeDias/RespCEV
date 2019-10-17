unica = [[], []]
print('-' * 50)
for rep in range(7):
    num = int(input(f'\rDigite o {rep+1}º Numero: '))
    if num % 2 == 0:
        unica[0].append(num)
    else:
        unica[1].append(num)
print('-' * 50)
unica[0].sort()
unica[1].sort()
print(f'Os Valores Pares Foram {unica[0]}')
print(f'Os Valores Impares Foram {unica[1]}')
print('-' * 50)
