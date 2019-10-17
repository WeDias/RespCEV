saldo = float(input('Quanto Dinheiro você tem ? '))
dolar = float(saldo / 3.27)
print('Com R${:.2f} Você pode comprar U${:.2f}!'.format(saldo, dolar))
