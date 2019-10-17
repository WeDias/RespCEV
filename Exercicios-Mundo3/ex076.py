lista = ('Caderno', 10.00,
         'Papel', 3.50,
         'Livro', 5,
         'Camisa', 20.90,
         'Caneta', 2.49,
         'Maça', 0.99,
         'Mochila', 100.30,
         'Agenda', 4.49)
print('-' * 39)
print(f'{"LISTA DE COMPRAS":^39}')
print('-' * 39)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
print('-' * 39)
