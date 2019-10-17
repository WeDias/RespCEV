km = float(input('Digite A Distancia Em KM: '))
if km <= 200:
    preco = float(0.50 * km)
    print('O Valor da passagem é de R${:.2f}'.format(preco))
else:
    preco = float(0.45 * km)
    print('O Valor da passagem é de R${:.2f}'.format(preco))
