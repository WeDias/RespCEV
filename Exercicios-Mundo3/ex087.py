matriz = [[], [], []]
soma = stc = maior = 0
print('-' * 50)
for l in range(3):
    for v in range(3):
        num = int(input(f'Digite O Valor Da Posição [{l},{v}]: '))
        matriz[l].append(num)
for n in matriz:
    for v in n:
        if v % 2 == 0:
            soma += v
for tc in range(0, 3):
    stc += matriz[tc][2]
for v in matriz[1]:
    if v > maior:
        maior = v
print('-' * 50)
print('SUA MATRIZ É:')
print(f'|{matriz[0][0]:^3}|{matriz[0][1]:^3}|{matriz[0][2]:^3}|')
print(f'|{matriz[1][0]:^3}|{matriz[1][1]:^3}|{matriz[1][2]:^3}|')
print(f'|{matriz[2][0]:^3}|{matriz[2][1]:^3}|{matriz[2][2]:^3}|')
print('-' * 50)
print(f'A Soma Dos Numeros Pares É: {soma}')
print(f'A Soma Dos Numeros Da Terceira Coluna É: {stc}')
print(f'O Maior Numero Da Segunda Linha É: {maior}')
print('-' * 50)
