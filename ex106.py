# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai
# aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

# Como eu fiz de maneira intuitiva
"""while True:
    print(f'''\033[42m~~~~~~~~~~~~~~~~~~~~~~~~
SISTEMA DE AJUDA PyHelp
~~~~~~~~~~~~~~~~~~~~~~~~\n\033[m''')
    pedido = input('Função ou Biblioteca (Digite FIM pra encerrar): ').strip().lower()
    if pedido == 'fim':
        print(f'\033[41mPROGRAMA ENCERRADO')
        break
    else:
        print(f'''\033[44m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Acessando o manural do comando {pedido}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\033[m''')
        print('\033[7m')
        help(pedido)
        print('\033[m')"""

# Como ele resolveu usando funções


def cor(num):  # 0:Vermelho / 1:Verde / 2:Azul / 3:Roxo / 4:Branco / 5:Limpa
    cores = ('\033[41;90m', '\033[42m', '\033[44m', '\033[45m', '\033[7m', '\033[m')
    return cores[num]


def titulo(msg):
    print('~' * (len(msg) + 4))
    print(f'  {msg}')
    print('~' * (len(msg) + 4))


def programa():
    while True:
        print(f'{cor(1)}', end='')
        titulo('SISTEMA DE AJUDA PyHelp')
        print(f'{cor(5)}', end='')

        pedido = input('Função ou Biblioteca (Digite FIM pra encerrar) > ').strip()

        if pedido.upper() == 'FIM':
            print(f'{cor(0)}', end='')
            titulo('PROGRAMA ENCERRADO')
            print(f'{cor(5)}', end='')
            break
        else:
            print(f'{cor(4)}', end='')
            titulo(f'{help(pedido)}')
            print(f'{cor(5)}', end='')


programa()
