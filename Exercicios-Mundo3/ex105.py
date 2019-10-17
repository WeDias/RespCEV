def notas(*notas, situ=False):
    """
    :param notas: Adicione quantas notas você quiser Ex.: 5, 10, 7.5, 8, 6, 9, 3, 8
    :param situ: (opcional) Mostra a Situação da Sala Se situ=True
    :return: Retorna um dicionario com o numero de notas informadas, a maior nota, a menor nota, a media das notas informadas, e a Situação se  situ=True Ex.:
    {'Notas': 8, 'Maior': 10, 'Menor': 3, 'Media': 7.0625, 'Situação': 'Boa'}
    """
    sala = dict()
    media = sum(notas)/len(notas)
    sala['Notas'] = len(notas)
    sala['Maior'] = max(notas)
    sala['Menor'] = min(notas)
    sala['Media'] = media
    if situ is True:
        if media >= 7:
            sala['Situação'] = 'Boa'
        elif 5 < media < 7:
            sala['Situação'] = 'Regular'
        elif media < 5:
            sala['Situação'] = 'Ruim'
    return sala


print(notas(5, 10, 7.5, 8, 6, 9, 3, 8, situ=True))
