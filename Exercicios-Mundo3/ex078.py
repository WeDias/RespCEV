lista = list()
for c in range(1, 6):
    lista.append(int(input('Digite Um Numero: ')))
print(f'\nO Menor valor Foi {min(lista)} Na {lista.index(min(lista)) + 1}ª Posição')
print(f'O Maior valor Foi {max(lista)} Na {lista.index(max(lista)) + 1}ª Posição')
