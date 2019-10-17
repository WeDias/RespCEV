matriz = [[], [], []]
col = 0
linha = 0
print('-' * 50)
for c in range(1, 10):
    num = int(input(f'Digite O Numero da Posição [{col},{linha}]: '))
    linha += 1
    if c < 4:
        matriz[0].append(num)
        if c == 3:
            col = 1
            linha = 0
    elif 3 < c < 7:
        matriz[1].append(num)
        if c == 6:
            col = 2
            linha = 0
    else:
        matriz[2].append(num)
print('-' * 50)
print('\nSUA MATRIZ É:\n')
print(f'|{matriz[0][0]:^3}|{matriz[0][1]:^3}|{matriz[0][2]:^3}|')
print(f'|{matriz[1][0]:^3}|{matriz[1][1]:^3}|{matriz[1][2]:^3}|')
print(f'|{matriz[2][0]:^3}|{matriz[2][1]:^3}|{matriz[2][2]:^3}|')
print('-' * 50)
