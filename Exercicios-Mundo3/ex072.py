numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'qunize', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = - 1
while num < 0 or num > 20:
    num = int(input('Digite Um Valor De 0 A 20: '))
print(f'Você Digitou O Número {numeros[num]}')
