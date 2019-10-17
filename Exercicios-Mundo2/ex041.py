from datetime import date
ano = int(input('Digite O Ano De Nascimento Do Atleta: '))
anoa = date.today().year
cate = anoa - ano
if  cate <= 9:
    print('\nO Atleta Tem {} Anos\nCategoria:\033[1;34m[MIRIM]\033[m'.format(cate))
elif 9 < cate <= 14:
    print('\nO Atleta Tem {} Anos\nCategoria:\033[1;34m[INFANTIL\033[m]'.format(cate))
elif 14 < cate <= 19:
    print('\nO Atleta Tem {} Anos\nCategoria:\033[1;34m[JUNIOR]\033[m'.format(cate))
elif 19 < cate <= 20:
    print('\nO Atleta Tem {} Anos\nCategoria:\033[1;34m[SÊNIOR]\033[m'.format(cate))
elif cate > 20:
    print('\nO Atleta Tem {} Anos\nCategoria:\033[1;34m[MASTER]\033[m'.format(cate))
