nome = str(input('Digite seu nome completo: ')).lower().strip()
print('Seu Nome Completo é: {}'.format(nome))
print('Seu Primeiro Nome é: {}'.format(nome.split()[0]))
print('Seu Ultimo Nome é: {}'.format(nome.split()[-1]))