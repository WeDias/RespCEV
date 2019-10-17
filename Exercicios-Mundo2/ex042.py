r1 = int(input('Digite a reta 1: '))
r2 = int(input('Digite a reta 2: '))
r3 = int(input('Digite a reta 3: '))

a = r1 < (r2 + r3)
b = r2 < (r1 + r3)
c = r3 < (r1 + r2)

if a and b and c is True:
    print('\nPode Foramr um Triangulo')
    if r1 == r2 and r1 == r3:
       print('É Um Triangulo EQUILÁTERO')
    elif r1 != r2 and r1 == r3 or r1 != r3 and r1 == r2:
        print('É Um Triangulo ISÓSCELES')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('É Um Triangulo ESCALENO')
else:
    print('Não Pode Formar um Triangulo')
