co = float(input('Digite o Cateto oposto: '))
ca = float(input('Digite o Cateto adjacente: '))
hip = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa desse triangulo é {:.2f}'.format(hip))