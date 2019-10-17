sexo = str(input('Digite Seu Sexo [M/F]: ')).upper()
while sexo != 'M' and sexo != 'F':
    print('\033[1;31mERRO! Digite apenas M ou F\033[m')
    sexo = str(input('Digite Seu Sexo [M/F]: ')).upper()
print('Você Digitou {}'.format(sexo))
