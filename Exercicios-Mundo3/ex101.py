def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} Anos: [VOTO NEGADO]'
    elif idade == 16 or idade == 17 or idade > 74:
        return f'Com {idade} Anos:[VOTO OPCIONAL]'
    elif idade > 17:
        return f'Com {idade} Anos:[VOTO OBRIGATORIO]'


print('-=' * 15)
ano = int(input('Data De Nascimento: '))
print(voto(ano))
print('-=' * 15)