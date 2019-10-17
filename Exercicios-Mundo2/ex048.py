soma = 0
print('A Soma Dos Impares Entre 1 E 500 É:')
for num in range(1, 501, 2):
    if num % 3 == 0:
        soma += num
        print(soma)
