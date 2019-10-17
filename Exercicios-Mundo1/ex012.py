item = float(input('Digite o Preço do produto: '))
desc = int(input('Digite o Valor do desconto: '))
preco = float(item - (item * desc / 100))
print('O produto com {}% de desconto, custara R${:.2f}!'.format(desc, preco))