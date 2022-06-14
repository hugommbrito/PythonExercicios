# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

# Como eu fiz de forma intuitiva:
"""from random import randint

print('\033[1mSou o seu computador e vou pensar em um número entre 0 e 10.'
      '\nTente adivinhas em que número estou pensando\033[m')
pc = randint(0, 10)
print(pc)
tentativas = 0
eu = 100

while eu != pc:
    eu = int(input('Qual o seu palpite? '))
    tentativas += 1
    if eu > pc:
        print('Huuuumm... Meu número é MENOR que esse. Tente novamente')
    elif eu < pc:
        print('Vishhh, errou! Meu número é MAIOR do que esse. Tente novamente.')
print(f'Você acertou na {tentativas}ª tentativa! Meu número é {pc}')"""

# Como ele resolveu no curso

from random import randint
pc = randint(0, 10)
print('''Sou o seu computador... Acabei de pensar em um número entre 0 e 10
Será que você consegue adivinhar qual é o número?''')
acertou = False
tentativas = 0

while not acertou:
    jogador = int(input('Qual é o seu palpite?'))
    tentativas += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador > pc:
            print('Menos... Tente novamente.')
        elif jogador < pc:
            print('Mais... Tente novamente.')
print('Acertou com {} tentativas. Parabéns'.format(tentativas))
