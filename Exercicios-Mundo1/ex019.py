import random
aluno1 = input('Digite o Nome do 1º Aluno: ')
aluno2 = input('Digite o Nome do 2º Aluno: ')
aluno3 = input('Digite o Nome do 3º Aluno: ')
aluno4 = input('Digite o Nome do 4º Aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print('O escolhido para limpar a lousa é {}!'.format(escolhido))
