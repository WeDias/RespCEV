frase = str(input('Digite Uma Frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, - 1, - 1):
    inverso += junto[letra]
if junto == inverso:
    print(junto, inverso, 'É Palindromo')
else:
    print(junto, inverso, 'Não É Palindromo')
