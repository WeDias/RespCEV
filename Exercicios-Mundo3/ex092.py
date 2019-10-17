from datetime import date
dados = dict()
print('-' * 50)
dados['nome'] = str(input('Digite O Nome: '))
anonasc = int(input('Digite O Ano: '))
dados['idade'] = (date.today().year - anonasc)
dados['ctps'] = int(input('Difgite A CTPS: '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano De Contratação: '))
    dados['salario'] = float(input('Salario: R$'))
    dados['aposentadoria'] = (date.today().year - anonasc) + (35 - (date.today().year - dados['contratação']))
print('-' * 50)
for c, i in dados.items():
    print(f'{c} = {i}')
print('-' * 50)