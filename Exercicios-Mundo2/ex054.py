import datetime
anoatual = datetime.date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Digite O Ano Em Que a {}ª Pessoa Nasceu: '.format(c)))
    if anoatual - ano >= 18:
        maior += 1
    else:
        menor += 1
print('\n{} Maiores De Idade E {} Menores De Idade'.format(maior, menor))