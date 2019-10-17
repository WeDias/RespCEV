salarioa = float(input('Digite o Salario do Funcionario: '))
aumento = int(input('Digite o Aumento que ele receberá: '))
salariod = salarioa + (aumento * salarioa / 100)
print('O funcionario que ganhava R${:.2f} com um aumento de {}%, passara a receber todo mês R${:.2f}'.format(salarioa, aumento, salariod))
