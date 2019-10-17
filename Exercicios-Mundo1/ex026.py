frase = str(input('Digite algo: ').lower().strip())
print('A frase tem {} letra a'.format(frase.count('a')))
print('A primeira letra a aparece no caractere {}'.format(frase.find('a')+1))
print('A ultima letra a aparece no caractere {}'.format(frase.rfind('a')+1))