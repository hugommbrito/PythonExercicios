#  Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
#  na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# l) Os últimos 4 colocados.
# l) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ("Palmeiras", "Santos", "Vasco da Gama", "Grêmio", "Flamengo", "Corinthians", "Internacional", "Cruzeiro",
         "São Paulo", "Atlético Mineiro", "Botafogo", "Fluminense", "Coritiba", "Bahia", "Goiás", "Guarani", "Sport",
         "Portuguesa", "Atlético Paranaense", "Vitória")

print('=-' * 30)
print(f'Lista de times do Campeonato Brasileiro são\n{times}')
print('=-' * 30)
print(f'5 primeiros colocados\n{times[:5]}')
print('=-' * 30)
print(f'4 últimos colocados\n{times[-4:]}')
print('=-' * 30)
print(f'Times em ordem alfabética\n{sorted(times)}')
print('=-' * 30)
print(f'O Flamengo está na {times.index("Flamengo")+1}ª colocação')
