num1 = int(input('Digite Um Numero Para Ver Sua Tabuada:'))
num2 = 0
for num2 in range(1, 11):
    mult = num1 * num2
    print('{}X{} = {}'.format(num1, num2, mult))
