# Crie um programa que faça o computador jogar Jokenpô com você.

# Primeira forma: Fiz de forma intuitiva como sabia e me alonguei muito no código para transformar 1, 2 e 3 em Pedra,
# Papel e Tesoura
"""from time import sleep
from random import randint

print('{:*^40}'.format(' VAMOS JOGAR JO-KEN-PO! '))
print('''\033[1mEscola a sua opção\033[m
\033[1;34m [ 1 ] PEDRA\033[m
\033[1;33m [ 2 ] PAPEL\033[m
\033[1;35m [ 3 ] TESOURA\033[m''')

player = int(input('\033[1mQual a sua jogada? \033[m'))
comp = randint(1, 3)

print('\033[1m*-' * 10, '\033[m')
print('\033[34mJO')
sleep(1.2)
print('\033[33mKEN')
sleep(1.2)
print('\033[35mPÔ!\033[m')
print('\033[1m*-' * 10, '\033[m')

if (player == 1 and comp == 3) or (player == 2 and comp == 1) or (player == 3 and comp == 2):
    if player == 1:
        player = 'PEDRA'
    elif player == 2:
        player = 'PAPEL'
    elif player == 3:
        player = 'TESOURA'
    if comp == 1:
        comp = 'PEDRA'
    elif comp == 2:
        comp = 'PAPEL'
    elif comp == 3:
        comp = 'TESOURA'
    print(f'\033[1mVocê escolheu {player} e o computador escolheu {comp}.\n \033[1;32mPARABÉNS, você venceu!\033[m')
elif (player == 1 and comp == 2) or (player == 2 and comp == 3) or (player == 3 and comp ==1):
    if player == 1:
        player = 'PEDRA'
    elif player == 2:
        player = 'PAPEL'
    elif player == 3:
        player = 'TESOURA'
    if comp == 1:
        comp = 'PEDRA'
    elif comp == 2:
        comp = 'PAPEL'
    elif comp == 3:
        comp = 'TESOURA'
    print(f'\033[1mVocê escolheu {player} e o computador escolheu {comp}.\n '
          f'\033[1;31mQue pena, o computador venceu.\033[m')
elif (player == 1 and comp == 1) or (player == 2 and comp == 2) or (player == 3 and comp == 3):
    if player == 1:
        player = 'PEDRA'
    elif player == 2:
        player = 'PAPEL'
    elif player == 3:
        player = 'TESOURA'
    if comp == 1:
        comp = 'PEDRA'
    elif comp == 2:
        comp = 'PAPEL'
    elif comp == 3:
        comp = 'TESOURA'
    print(f'\033[1;33mVocês dois escolheram {player}, vocês empataram!')"""

# Segunda forma: Como ele faz no vídeo, usando uma lista para transformar os ítens

from time import sleep
from random import randint

print('{:*^40}'.format(' VAMOS JOGAR JO-KEN-PO! '))
print('''\033[1mEscola a sua opção\033[m
\033[1;34m [ 0 ] PEDRA\033[m
\033[1;33m [ 1 ] PAPEL\033[m
\033[1;35m [ 2 ] TESOURA\033[m''')

player = int(input('\033[1mQual a sua jogada? \033[m'))
comp = randint(0, 2)
item = ('PEDRA', 'PAPEL', 'TESOURA')

print('\033[1m*-' * 10, '\033[m')
print('\033[34mJO')
sleep(0.5)
print('\033[33mKEN')
sleep(0.5)
print('\033[35mPÔ!\033[m')
print('\033[1m*-' * 10, '\033[m')

if (player == 0 and comp == 2) or (player == 1 and comp == 0) or (player == 2 and comp == 1):
    print(f'\033[1mVocê escolheu {item[player]} e o computador escolheu {item[comp]}.'
          f'\n \033[1;32mPARABÉNS, você venceu!\033[m')
elif (player == 0 and comp == 1) or (player == 1 and comp == 2) or (player == 2 and comp == 0):
    print(f'\033[1mVocê escolheu {item[player]} e o computador escolheu {item[comp]}.\n '
          f'\033[1;31mQue pena, o computador venceu.\033[m')
elif (player == 0 and comp == 0) or (player == 1 and comp == 1) or (player == 2 and comp == 2):
    print(f'\033[1;33mVocês dois escolheram {item[player]}, vocês empataram!')
