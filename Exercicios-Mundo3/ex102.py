def fatorial(n, m=False):
    """
    :param n: O Numero Para Saber O Fatorial EX.: fatorial(5) = 120.
    :param m:(Opcional) Mostrar A Conta EX.: factorial(5, True) = 5x1 5x2 5x3 5x4 = 120.
    :return: Retorna o Fatorial De Acordo Com os Parametros Acima.
    """
    fato = n
    for c in range(1, n):
        fato *= c
        if m is True:
            print(f'{n}X{c}', end=', ')
    if m is True:
        print(f'= {fato}')
        print(f'O Fatorial De {n} É {fato}')
    if m is False:
        print(f'O Fatorial De {n} É {fato}')


print(help(fatorial))
num = int(input('Digite Um Numero: '))
opc = str(input('Deseja Ver O Calculo[S/N]: ')).upper()
if opc == 'S':
    opc = True
else:
    opc = False
fatorial(num, opc)