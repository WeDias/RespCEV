cont = soma = 0
print('Digite 999 Para Parar')
while True:
    num = int(input(f'Digite O {cont + 1}º Numero:'))
    if num == 999:
        break
    else:
        cont += 1
        soma += num
print(f'A Soma Foi De {soma} E Foram Digitados {cont} Numeros')
