termo1 = int(input('Digite O Primeiro Termo Da P.A.: '))
razao = int(input('Digite A Razão Da P.A.: '))
termos = int(input('Digite O Numero De Termos Que Você Deseja Ver: '))
cont = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont < total * razao:
        print(termo1 + cont)
        cont += razao
    mais = int(input('Quantos Termos Você Quer Mostrar A Mais: '))
