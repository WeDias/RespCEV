#50 20 10 1
print('+' * 30)
print(' ' * 6, 'CAIXA ELETRONICO')
print('+' * 30)
sacar = int(input('Quanto Deseja Sacar: R$'))
print('+' * 30)
nota50 = 0
nota20 = 0
nota10 = 0
nota1 = 0
resto = 0
if sacar >= 50:
    nota50 = sacar // 50
    resto = sacar % 50
    nota20 = resto // 20
    resto = resto % 20
    nota10 = resto // 10
    resto = resto % 10
    nota1 = resto // 1
elif 50 > sacar >= 20:
    nota20 = resto // 20
    resto = resto % 20
    nota10 = resto // 10
    resto = resto % 10
    nota1 = resto // 1
elif 20 > sacar >= 10:
    nota10 = resto // 10
    resto = resto % 10
    nota1 = resto // 1
elif 10 > sacar >= 1:
    resto = resto % 10
    nota1 = resto // 1
print(f'{nota50} Notas De R$50\n{nota20} Notas De R$20\n{nota10} Notas De R$10\n{nota1} Notas De R$1')
print('+' * 30)
