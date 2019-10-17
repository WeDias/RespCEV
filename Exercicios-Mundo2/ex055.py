maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Digite O Peso Da {}ª Pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('\nO Maior Peso Digitado Foi {}\nO menor Peso Digitado Foi {}'.format(maior, menor))
