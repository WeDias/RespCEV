total = caro = baratov = 0
baraton = ''
add = 'S'
print('-' * 34)
print(' ' * 8, 'LISTA DE COMPRAS')
print('-' * 34)
while add == 'S':
    produto = str(input('Nome Do Produto: ')).strip().upper()
    preco = float(input('Preço: R$'))
    add = str(input('Adicinar Outro Produto[S/N]: ')).strip().upper()
    total += preco
    if preco < baratov or baratov == 0:
        baratov = preco
        baraton = produto
        if preco > 1000:
            caro += 1
    elif preco > 1000:
        caro += 1
    elif add == 'N':
        break
print('-' * 34)
print('O Total Foi De R${:.2f}'.format(total))
print('O Produto Mais Barato Foi: {} R${:.2f}'.format(baraton, baratov))
print('{} Prdutos Acima de R$1000'.format(caro))
