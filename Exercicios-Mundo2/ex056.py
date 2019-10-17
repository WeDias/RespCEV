media = 0
hvelho = 0
ivelho = 0
mulhernova = 0
for c in range(1, 5):
    print('-----{}ª Pessoa-----'.format(c))
    nome = str(input('Nome: ')).upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F] :')).upper()
    media += idade
    if sexo == 'M' and idade > ivelho:
        hvelho = nome
        ivelho = idade
    elif sexo == 'F' and idade < 20:
        mulhernova = mulhernova + 1
print('-' * 19)
print('\nA Media De idade Do Grupo É:  {} Anos'.format(media / 5))
print('O Homem Mais Velho É: {}'.format(hvelho))
if mulhernova == 1:
    print('Existe 1 Mulher Com Menos De 20 Anos')
else:
    print('Existem {} Mulheres Com Menos De 20 Anos'.format(mulhernova))
