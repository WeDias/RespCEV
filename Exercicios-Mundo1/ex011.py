largura = float(input('Digite a Largura da Parede: '))
altura = float(input('Digite a Altura da Parede: '))
area = float(largura * altura)
tintanec = area / 2
print('Em uma parede de {:.2f} Metros quadrados, é necessario {:.2f} Litros de Tinta!'.format(area, tintanec))
