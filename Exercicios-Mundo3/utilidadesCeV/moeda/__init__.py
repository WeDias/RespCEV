def aumentar(num, perc, formatar=True):
    num = num + num * perc / 100
    if formatar:
        num = moeda(num)
    return num


def diminuir(num, perc, formatar=True):
    num = num - num * perc / 100
    if formatar:
        num = moeda(num)
    return num


def dobro(num, formatar=True):
    num = num * 2
    if formatar:
        num = moeda(num)
    return num


def metade(num, formatar=True):
    num = num / 2
    if formatar:
        num = moeda(num)
    return num


def moeda(num):
    return f'R${num:.2f}'


def resumo(num, aument, diminui):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado:  {moeda(num).rjust(10)}')
    print(f'Dobro do preço:   {dobro(num).rjust(10)}')
    print(f'Metade do preço:  {metade(num).rjust(10)}')
    print(f'{aument}% de aumento:   {aumentar(num, aument).rjust(10)}')
    print(f'{diminui}% de redução:   {diminuir(num, diminui).rjust(10)}')
    print('-' * 30)
