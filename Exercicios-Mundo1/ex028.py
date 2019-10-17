import random
user = int(input('Digite um Número de 0 a 5: '))
pc = random.randint(0, 5)
if user == pc:
    print('O Computador esolheu o Número {}\nPARABENS! VOCÊ ACERTOU !'.format(pc))
else:
    print('O Computador escolheu o Número {}\nVOCÊ PERDEU !'.format(pc))
