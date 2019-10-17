def area(l, c):
    print(f'A Area Do Terreno DE {l}m X {c}m É: {l * c:.2f} m2')
    print('-' * 30)


print('-' * 30)
print('CALCULANDO AREA DO TERRENO:')
print('-' * 30)
largura = float(input('Digite A Largura: '))
comprimento = float(input('Digite O Comprimento: '))
area(largura, comprimento)