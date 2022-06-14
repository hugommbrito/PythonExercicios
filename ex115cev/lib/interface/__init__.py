def leiaInt(msg):
    while True:
        num = input(msg).strip()
        try:
            nInt = int(num)

        except (ValueError, TypeError):
            print(f'\033[31m"{num}" não é um número inteiro, tente novamente.\033[m')

        else:
            return nInt

def linha(tam = 42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(len(linha())))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc