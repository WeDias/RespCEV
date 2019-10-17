sala = list()
aluno = list()
while True:
    print('-' * 50)
    aluno.append(str(input('Digite O Nome Do Aluno: ')).upper())
    for c in range(2):
        aluno.append(float(input(f'Digite A {c +1}ª Nota: ')))
    sala.append(aluno[:])
    aluno.clear()
    print('-' * 50)
    continuar = str(input('Adicionar Outro Aluno[S/N]: ')).upper()
    if continuar == 'N':
        break
print('-' * 50)
cont = 0
situ = ''
for alunos in sala:
    media = (alunos[1] + alunos[2]) / 2
    if media < 5:
        situ = '\033[31m[RECUPERAÇÃO]\033[m'
    elif media > 4:
        situ = '\033[32m[APROVADO]\033[m'
    print(f'{cont:^1}', f'|{alunos[0]:^11}', f'| Media: {media:.1f}', f'| {situ}')
    cont += 1
print('-' * 50)
opc = str(input('Quer Ver As Notas De Cada Aluno[S/N]: ')).upper()
if opc == 'S':
    while True:
        num = int(input('Digite o Numero Do Aluno Que Você Deseja Ver As Notas: '))
        print(f'As Notas De {sala[num][0]} Foram {sala[num][1:]}')
        opc = str(input('Outro Aluno[S/N]: '))
        if opc == 'N':
            break
