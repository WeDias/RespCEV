aluno = dict()
aluno['nome'] = str(input('Nome Do Aluno: ')).upper()
aluno['media'] = float(input(f'Media Do {aluno["nome"]}: '))
if aluno['media'] > 6:
    aluno['situação'] = '[APROVADO]'
else:
    aluno['situação'] = '[REPROVADO]'
print(f'\nO aluno {aluno["nome"]}')
print(f'Media: {aluno["media"]}')
print(f'Situação: {aluno["situação"]}')
