#  Vamos criar um menu em Python, usando modularização.

def menu():
    while True:
        print('-' * 30)
        print('MENU PRINCIPAL'.center(30))
        print('-'*30)
        print('\033[33m1\033[m - \033[34mVer pessoas cadastradas\033[m')
        print('\033[33m2\033[m - \033[34mCadastrar nova pessoa\033[m')
        print('\033[33m3\033[m - \033[34mSair do Programa\033[m')
        print('-' * 30)

        try:
            opcao = int(input('\033[33mSua opção: \033[m'))
        except ValueError:
            print('\033[31mERRO: Digite um número inteiro válido.\033[m')
            continue

        if opcao not in (1, 2, 3):
            print('\033[31mERRO: Esta não é uma opção válida.\033[m')
        else:
            break

    return opcao

from time import sleep

def opcoes(op):
    if op == 1:
        print('-' * 30)
        print('Opção 1'.center(30, '~'))
        print('-' * 30)
        sleep(3)
        menu()

    elif op == 2:
        print('-' * 30)
        print('Opção 2'.center(30, '~'))
        print('-' * 30)
        sleep(3)
        menu()

    elif op == 3:
        print('-' *30)
        print('ENCERRANDO O SISTEMA, ATÉ LOGO!'.center(30, '~'))
        print('-' * 30)

