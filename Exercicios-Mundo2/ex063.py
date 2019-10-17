num = int(input('Quantos números da sequencia de Fibonacci você quer mostrar: '))
c = 1
termo = 0
t1 = 0
t2 = 1
while c <= num:
    print('{} - '.format(termo), end=' ')
    termo = t1 + t2
    if c >= 2:
        termo = t1 + t2
        t1 = t2
        t2 = termo
    c += 1
print('FIM')
