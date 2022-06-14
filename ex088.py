# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
print('-' * 40)
print('JOGO DA MEGA SENA'.center(40))
print('-' * 40)
numDeJogos = int(input('Quantos jogos você quer que eu sorteie? '))
jogoProvisorio = []
jogos = []

for j in range(0, numDeJogos):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogoProvisorio:
            jogoProvisorio.append(num)
            cont += 1
        if cont >= 6:
            break
    jogoProvisorio.sort()
    jogos.append(jogoProvisorio[:])
    jogoProvisorio.clear()

print('+=' * 20)
for a in range(0, numDeJogos):
    print(f'{jogos[a]}'.center(40))
    sleep(0.5)
# print('+=' * 20)
print('< BOA SORTE >'.center(40, '~'))
