import math
ang = float(input('Digite o valor do Ângulo: '))
seno = float(math.sin(math.radians(ang)))
coso = float(math.cos(math.radians(ang)))
tang = float(math.tan(math.radians(ang)))
print('O Seno Do Ângulo {0} é {1:.3f}\nO Cosseno Do Ângulo {0} é {2:.3f}\nA Tangente Do Ângulo {0} é {3:.3f}'.format(ang, seno, coso, tang))
