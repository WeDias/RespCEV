# Conversão de escalas Celsius, Kelvin e Fahrenheit
celsius = float(input('Digite Quantos Graus Celsius: '))
kelvin = float(celsius + 273)
fahrenheit = float(1.8 * celsius + 32)
print('{}ºC é igual a {}ºK ou {:.2f}ºF'.format(celsius, kelvin, fahrenheit))
