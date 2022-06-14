# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.


# Como eu fiz com pesquisa aprendendo a usar a formula LAMBDA para esse porósito
from random import randint
from time import sleep

print('JOGO DE DADOS'.center(36), '\n')

jogadores = {}
for c in range(0, 4):
    jogadores['jogador'+str(c+1)] = randint(1, 6)

for k, v in jogadores.items():
    print(f'O {k} tirou {v} no dado.'.center(36))
    sleep(0.7)

print('=-' * 18)
sleep(0.5)
print('<<< RANKING DOS JOGADORES >>>'.center(36))
sleep(1.5)

ordenado = {k: v for k, v in sorted(jogadores.items(), key=lambda v: v[1], reverse=True)}
cont = 1
for k, v in ordenado.items():
    print(f'{cont}º lugar: {k} com {v} pontos.'.center(36))
    sleep(0.7)
    cont += 1

# Como ele fez no vídeo usando a biblioteca OPERATOR (nesse caso, gostei mais da minha solução)

"""from random import randint
from time import sleep
from operator import itemgetter

jogo = { 'Jogador1': randint(1, 6),
          'Jogador2': randint(1, 6),
          'Jogador3': randint(1, 6),
          'Jogador4': randint(1, 6)}
print('Valores Sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)

print('=-' * 15)
print('   == RANKING DOS JOGADORES ==')
ranking = list()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'O {i+1}º lugar foi o  {v[0]} que tirou {v[1]}')
    sleep(0.5)"""
