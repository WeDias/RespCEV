sal = float(input('Digite o Salario do Funcionario: '))
if sal > 1250:
    print('Com um aumento ele passara a receber R${:.2f}'.format(sal + (sal / 100 * 10)))
else:
    print('Com um aumneto ele passara a receber R${:.2f}'.format(sal + (sal / 100 * 15)))
