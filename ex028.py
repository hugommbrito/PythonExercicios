# Escreva um programa que faça o computador "pensar" em um núemro inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número. O programa deverá tentar escrever na tela se o usuário venceu ou perdeu o jogo.

# Primeira forma: Fazendo o jogo de forma mais complexa usando os aprendizados do curso "Python for Everbody" (coursera)
from random import choice

print('Inicio do jogo, tente adivinhar em que número estou pensando. \n DICA: Só sei contar até 5 ;).')
range = [1, 2, 3, 4, 5]
right = 0
wrong = 0
rounds = 0
while True:
    pc_num = choice(range)  # PC escolhe um número

    user_num = input('Qual o seu palpite? ')  # Usuário escolhe um número
    if user_num == 'end game':  # Gatilho para o fim de jogo, sai do loop
        break

    try:  # Testa se o usuário colocou um número inteiro e exibe mensagem de erro ou continua normalmente
        user_num == int(user_num)
    except:
        print('Você é burro??? Te falei pra colocar um número! Tenta de novo.')
        continue

    if int(user_num) == pc_num:  # checa se acertei ou errei o número e soma +1 em rounds ou em right/wrong
        print('\033[1;32mParabéns, você acertou, eu estava mesmo pensando em {}\033[m'.format(pc_num))
        print('---*' * 14)
        right = right + 1
        rounds = rounds + 1
    else:
        print('\033[1;31mNão foi dessa vez, eu estava pensando em {}\033[m'.format(pc_num))
        print('*=' * 25)
        wrong = wrong + 1
        rounds = rounds + 1

    print('Até agora você acertou {} vezes e errou {} vezes.'.format(right, wrong))

right_rate = (right / rounds) * 100
wrong_rate = (wrong / rounds) * 100

print('\nFIM DE JOGO')
print('Você jogou {} partidas, acertou {} vezes e errou {}. \n TAXA DE ACERTOS: {:.2f}% \n TAXA DE ERROS: {:.2f}%'
      .format(rounds, right, wrong, right_rate, wrong_rate))

# Segunda Forma: Como ele fez no vídeo

'''from random import randint
from time import sleep

computador = randint(1, 5)
print('-=-' * 22)
print('Vou pensar em um número entre 1 e 5. Tente adivinhar qual é...')
print('-=-' * 22)
jogador = int(input('Qual o seu palpite? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você me venceu.')
else:
    print('Tente de novo, eu pensei no número {}.'.format(computador))'''
