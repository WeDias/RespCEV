produtov = float(input('Digite O Valor Do Produto: R$'))
formapag = int(input('[1]DINHEIRO/CHEQUE\n[2]CARTÃO\n'))
if formapag == 1:
    print('Preço Final: R${:.2f}'.format(produtov - (produtov * 10/100)))
elif formapag == 2:
    vezes = int(input('Em Quantas Vezes: '))
    if vezes == 1:
        print('\nR${:.2f} EM 1x No Cartão\nPreço Final: R${:.2f}'.format(produtov - (produtov * 5 / 100) / vezes, produtov - (produtov * 5 / 100)))
    elif vezes == 2:
        print('\nR${:.2f} EM 2x No Cartão\nPreço Final: R${:.2f}'.format(produtov / vezes, produtov))
    elif vezes >= 3:
        print('\nR${:.2f} EM {}x No Cartão\nPreço Final: R${:.2f}'.format(produtov + (produtov * 20 / 100) / vezes, vezes, produtov + (produtov * 20 / 100)))
else:
    print('Erro Tente Novamente')
