from random import randint
num = (randint(1, 999), randint(1, 999), randint(1, 999), randint(1, 999), randint(1, 999))
print(f'Os Valores Sorteeados Foram: ', end='')
for n in num:
    print(f'{n}', end=' ')
print(f'\O Menor Numero Foi: {min(num)}')
print(f'O Maior Numero Foi: {max(num)}')
