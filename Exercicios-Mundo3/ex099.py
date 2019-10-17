def maior(num):
    maior = 0
    for v in num:
        if v > maior:
            maior = v
    print('=' * 30)
    print(f'O Maior Numero Foi {maior}')
    print('=' * 30)


numeros = []
while True:
    num = int(input('Digite Um Numero: [999]Para Parar '))
    if num != 999:
        numeros.append(num)
    else:
        break
print(numeros)
maior(numeros)