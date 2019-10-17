def contador():
    from time import sleep
    sleep(1)
    print(f'A) De 1 Até 10, De 1 Em 1:', end=' ')
    for n in range(1, 11):
        sleep(1)
        print(f'\033[31m{n}\033[m', end=', ')
    print()
    sleep(1)
    print(f'B) De 10 Até 0, De 2 Em 2:', end=' ')
    for n in range(10, -1, -2):
        sleep(1)
        print(f'\033[31m{n}\033[m', end=', ')
    print()
    print(f'Agora É Sua Vez De Criar Uma Contagem')
    i = int(input('Digite O Inicio: '))
    f = int(input('Digite O Final: '))
    m = int(input('De Quanto Em Quanto: '))
    if m == 0:
        print(f'C) De {i} Até {f} De 1 Em 1:', end=' ')
    else:
        print(f'C) De {i} Até {f} De {m} Em {m}:', end=' ')
    if i < f and 0 != m != -1:
        for n in range(i, f, m):
            sleep(1)
            print(f'\033[31m{n}\033[m', end=', ')
    if i > f and 0 != m != -1:
        for n in range(i, f - m, -m):
            sleep(1)
            print(f'\033[31m{n}\033[m', end=', ')
    if m < 0:
        for n in range(i, f +m, m):
            sleep(1)
            print(f'\033[31m{n}\033[m', end=', ')
    if i > f and m == 0:
        for n in range(i, f, -1):
            sleep(1)
            print(f'\033[31m{n}\033[m', end=', ')
    if i < f and m == 0:
        for n in range(i, f, 1):
            sleep(1)
            print(f'\033[31m{n}\033[m', end=', ')


contador()