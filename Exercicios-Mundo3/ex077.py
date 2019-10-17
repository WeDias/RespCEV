lista = ('CASA', 'PORTA', 'LOJA',
         'TORTA', 'BOLSA', 'CELULAR',
         'TECLADO', 'ARROZ', 'BATATA',)
for p in lista:
    print(f'\nNa Palavra {p} Temos: ', end='')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(f'{letra}', end='')
