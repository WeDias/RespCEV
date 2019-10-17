exp = str(input('Digite Uma Expressão: '))
abre = 0
for carac in exp:
    if carac == '(':
        abre += 1
    elif carac == ')':
        abre -= 1
if abre == 0:
    print('Expressão Válida')
else:
    print('Expressão Invalida')
