dias = int(input('Digite o numero de dias que o carro ficou alugado: '))
km = float(input('Digite a Quilometragem do carro nesse periodo: '))
valor = float(dias * 60 + 0.15 * km)
print('Com um carro alugado por {} Dias e percorrido {}Km, O valor a ser pago é R${:.2f}'.format(dias, km, valor))
