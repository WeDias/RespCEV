from random import randint
num = (randint(1, 999), randint(1, 999), randint(1, 999), randint(1, 999), randint(1, 999))
print(f'Os Valores Sorteados Foram: ', end='')
menor = maior = 0
for n in num:
    print(f'{n}', end=' ')
    if menor == 0 and maior == 0:
        menor = n
        maior = n
    elif n < menor:
        menor = n
    elif n > maior:
        maior = n
print(f'\nO Menor Numero Foi: {menor}')
print(f'O Maior Numero Foi: {maior}')
