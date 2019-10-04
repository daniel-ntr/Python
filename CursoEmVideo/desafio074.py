# TIMES DE FUTEBOL EM TUPLA

times = ('Flamengo', 'Palmeiras', 'Santos', 'Corinthians', 'Internacional', 'São Paulo',
         'Bahia', 'Grêmio', 'Athletico-PR', 'Atlético', 'Botafogo', 'Goiás', 'Vasco da Gama',
         'Ceará SC', 'Fortaleza', 'Fluminense', 'Cruzeiro', 'CSA', 'Avaí', 'Chapecoense')
posicao = 0
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O {times[19]} está na {times.index("Chapecoense") + 1}ª posição')
print('-=' * 15)
