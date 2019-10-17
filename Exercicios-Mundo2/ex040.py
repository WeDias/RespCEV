repetir = 's'
while repetir == 's':
    print('-' * 33)
    nome = str(input('\033[36mDigite O Nome Do Aluno: '))
    nota1 = float(input('Digite A Primeira Nota: '))
    nota2 = float(input('Digite A Segunda Nota:\033[m '))
    if ((nota1 + nota2) / 2) < 5:
     print('\033[36mMédia Do Aluno: {} \033[1;31m[REPROVADO]\033[m'.format((nota1 + nota2) / 2))
    elif 5 <= ((nota1 + nota2) / 2 ) <= 6.9:
        print('\033[36mMédia Do Aluno: {} \033[1;31m[RECUPERAÇÃO]\033[m'.format((nota1 + nota2) / 2))
    elif ((nota1 + nota2) / 2) >= 7:
        print('\033[36mMédia Do Aluno: {} \033[1;32m[APROVADO]\033[m'.format((nota1 + nota2) / 2))
print('-' * 33)
