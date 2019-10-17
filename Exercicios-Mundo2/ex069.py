totalpessoas = 0
homens = 0
maiores = 0
mulheresnovas = 0
print('\033[1;34m~' * 25, '\n  CADAESTRE UMA PESSOA')
print('\033[1;34m~\033[m' * 25)
while True:
    totalpessoas += 1
    print(f'{totalpessoas}ª PESSOA')
    idade = 0
    while idade not in range(1, 200):
        idade = int(input('Digite A Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite O Sexo[M/F]: ').strip().upper())
    print('-' * 25)
    if sexo == 'M':
        if idade >= 18:
            maiores += 1
            homens += 1
        elif idade < 18:
            homens += 1
    elif sexo == 'F':
        if idade >= 18:
            if idade < 20:
                maiores += 1
                mulheresnovas += 1
            elif idade >= 20:
                maiores += 1
        elif idade > 20:
            maiores += 1
        elif idade < 18:
            mulheresnovas += 1
    continuar = ' '
    while continuar not in ('SN'):
        continuar = str(input('Deseja Continuar[S/N]: ')).upper()
    print('-' * 25)
    if continuar == 'N':
        break
print(f'{homens} São Homens, {maiores} São Maiores E {mulheresnovas} São Mulheres Com Menos De 20 Anos')
