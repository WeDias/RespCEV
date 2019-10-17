valorcasa = float(input('Digite O Valor Da Casa: R$'))
sal = float(input('Digite O Seu Salario: R$'))
anos = int(input('Em Quantos Anos Deseja Pagar O Emprestimo: '))
if (valorcasa / 12 / anos) <= (sal * 30 / 100):
    print('\n\033[1;32mEmprestimo Aprovado\033[m')
elif (valorcasa / 12 / anos) >= (sal * 30/100):
    print('\n\033[1;31mEmprestimo Negado\033[m')
print('A Prestação Sera De R${:.2f}\nVolte Sempre!'.format(valorcasa / 12 / anos))
