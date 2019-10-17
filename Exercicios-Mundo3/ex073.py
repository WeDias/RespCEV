times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético', 'Atlético-PR', 'Cruzeiro',
         'BotaFogo', 'Santos', 'Bahia', 'Corinthians', 'Ceará SC', 'Fluminense', 'Vasco', 'Chapecoense', 'América-MG',
         'Sport Recife', 'EC Vitória', 'Paraná')
print(f'Os 5 Primeiros Colocados Foram:\n{times[0:5]}')
print(f'Os 4 Ultimos Colocados Foram:\n{times[16:]}')
print(f'Em Ordem Alfabetica Fica:\n{sorted(times)}')
print(f'A Chapecoense Está Na {times.index("Chapecoense") + 1}ª Posição')
