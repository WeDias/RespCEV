termo1 = int(input('Digite O Primeiro Termo Da P.A.: '))
razao = int(input('Digite A Razão Da P.A.: '))
cont = 0
while cont < 10 * razao:
    print(termo1 + cont)
    cont += razao
