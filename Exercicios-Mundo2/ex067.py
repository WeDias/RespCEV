from time import sleep
cont = 0
print('-' * 36)
while True:
    num = int(input('\033[1mQuer Ver A Tabuada De Qual Numero:\033[m '))
    while num > 0:
        cont += 1
        mult = num * cont
        sleep(0.25)
        print(f'\033[1;31m{num}\033[m X \033[1;31m{cont}\033[m = \033[1;31m{mult}\033[m')
        if cont == 10:
            cont = 0
            break
    print('-' * 36)
    if num < 0:
        break
