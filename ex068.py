#  Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
#  mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

win = 0
from random import randint

print('=='*20)
print('\033[1;31m', ' PAR OU ÍMPAR '.center(39, '~'), '\033[m')
print('=='*20)

while True:
    print('-'*30)
    pl_n = int(input('Que número você escolhe? '))  # pl_n se refere é PLAYERS NUMBER
    pl_c = str(input('Você escolhe Ímpar ou Par? [I/P] ')).strip()[0]  # pl_c se refere a PLAYERS CHOICE
    pc = randint(0, 11)

    if pl_c not in 'PpIiÍí':
        print('Opção inválida')
        continue
    if pl_c in 'Pp' and (pl_n+pc) % 2 == 0:
        print('\n', '^'*30)
        print(f'Parabéns, você ganhou!')
        print(f'Você escolheu {pl_n} e eu escolhi {pc}, {pl_n + pc} é PAR!')
        win += 1
    elif pl_c in 'IiÍí' and (pl_n + pc) % 2 != 0:
        print('\n', '~'*30)
        print('Parabéns, você ganhou!')
        print(f'Você escolheu {pl_n} e eu escolhi {pc}, {pl_n + pc} é ÍMPAR!')
        win += 1
    else:
        break

print('*'*30)
print(f'Agora não deu! Você perdeu.\n Você escolheu {pl_n} e eu escolhi {pc}.'
      f'\nNo decorrer do jogo você acumulou {win} vitórias.')
