print('+' * 30)
print(' ' * 6, 'CAIXA ELETRONICO')
print('+' * 30)
sacar = int(input('Quanto Deseja Sacar: R$'))
print('+' * 30)
nota50 = sacar // 50
resto = sacar % 50
nota20 = resto // 20
resto = resto % 20
nota10 = resto // 10
resto = resto % 10
nota1 = resto // 1
if nota50 > 0:
    print(f'{nota50} Notas de R$50')
if nota20 > 0:
    print(f'{nota20} Notas de R$20')
if nota10 > 0:
    print(f'{nota10} Notas de R$10')
if nota1 > 0:
    print(f'{nota1} Notas de R$1')
print('+' * 30)
