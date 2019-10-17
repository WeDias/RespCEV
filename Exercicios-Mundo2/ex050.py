rep = 0
soma = 0
for rep in range(1, 6):
    num1 = int(input('DIGITE UM NUMERO: '))
    if num1 % 2 == 0:
        soma += num1
print(soma)
