def leia_dinheiro(txt):
    while True:
        entrada = input(txt)
        try:
            if entrada.count(',') > 0:
                entrada = entrada.replace(',', '.')
            entrada = float(entrada)
            return entrada
        except:
            if entrada.count('.') > 0:
                entrada = entrada.replace('.', ',')
            print(f'\033[1;4;31mERRO: "{entrada}" é um valor inválido !\033[m')
