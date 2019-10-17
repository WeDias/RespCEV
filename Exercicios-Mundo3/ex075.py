num = (int(input('Digite Um Numero: ')), int(input('Digite Outro Numero: ')), int(input('Digite Outro Numero: ')), int(input('Digite O Ultimo Numero: ')))
print(f'\nForam Digitados Os Numeros:\n', end='')
pares = 0
for n in num:
    print(n)
    if n % 2 == 0:
        pares += 1
print('-' * 30)
print(f'Apareceu o 9 {num.count(9)} Vezes')
if 3 in num:
    print(f'O Numero 3 Apareceu Na {num.index(3) + 1}ª Vez')
print(f'{pares} São Pares')
