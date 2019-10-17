num = int(input('Digite Um Numero Para Descobrir Seu Fatorial: '))
cont = num
fatorial = 1
while cont > 0:
    fatorial = fatorial * cont
    cont -= 1
print(fatorial)
