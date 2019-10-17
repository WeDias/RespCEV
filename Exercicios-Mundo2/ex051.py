termo1 = int(input('Digite O Primeiro Termo Da P.A.: '))
razao = int(input('Digite A Razão Da P.A.: '))
decimotermo = termo1 + (10-1) * razao
for contador in range(termo1, decimotermo + razao, razao):
    print(contador)
print('FIM')
