velo = float(input('Digite a velocidade do carro em KM/H: '))
if velo > 80:
    multa = float((velo - 80) * 7.00)
    print(f'Você exedeu o Limite De 80KM/H Permitido, Sua Velocidade Foi de {velo:.0f}KM/H !! A Multa é de R${multa:.2f}')
else:
    print('Você Não Exedeu o Limite Permitido!!')
