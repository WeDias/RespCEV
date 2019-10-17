from time import sleep
print('\033[31m-\033[m' * 33)
print(' ' * 10, '\033[1;31mCALCULO IMC\033[m')
print('\033[31m-\033[m' * 33)
peso = float(input('Digite Seu Peso em KG: '))
altura = float(input('Digite Sua Altura em CM: '))
imc = peso / (altura / 100) ** 2
sleep(0.5)
if imc <= 16.9:
    print('\033[1;33mATENCĀO!\033[m Seu IMC é de {:.2f}, Você esta muito abaixo do peso ideal'.format(imc))
elif 17 <= imc <= 18.4:
    print('\033[1;33mATENCĀO!\033[m Seu IMC é de {:.2f}, Você esta abaixo do peso ideal'.format(imc))
elif 18.5 <= imc <= 24.9:
    print('\033[1;32mPARABENS!\033[m Seu IMC é de {:.2f}, Você esta no peso ideal'.format(imc))
elif 25.9 <= imc <= 29.9:
    print('\033[1;33mATENCĀO!\033[m Seu IMC é de {:.2f}, Você esta acima do peso ideal'.format(imc))
elif 30 <= imc <= 34.9:
    print('\033[1;33mATENCĀO!\033[m Seu IMC é de {:.2f}, Você esta com Obesidade Grau I'.format(imc))
elif 35 <= imc <= 40:
    print('\033[1;33mATENCĀO!\033[m Seu IMC é de {:.2f}, Você esta com Obesidade Grau II'.format(imc))
elif 40 <= imc:
    print('\033[1;33mATENCĀO!\033[m Seu IMC é de {:.2f}, Você esta com Obesidade Grau III'.format(imc))
print('\033[31m-\033[m' * 33)