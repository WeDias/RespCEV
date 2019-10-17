continuar = 's'
media = 0
maior = 0
menor = 0
contador = 0
while continuar == 's':
    num = int(input('Digite Um Numero: '))
    continuar = str(input('Deseja Digitar Outro Numero[S/N]: ')).lower()
    contador += 1
    media = (media + num) / contador
    if contador == 1:
        maior = num
        menor = num
    elif num < menor:
        menor = num
    elif num > maior:
        maior = num
print('A Media Entre Esses Numeros É {}, O Maior Numero É {} E O Menor Numero É {}'.format(media, maior, menor))