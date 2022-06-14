def aumentar(n, p=10, formatar=True):
    resposta = n * (1+(p/100))
    return resposta if not formatar else moeda(resposta)


def diminuir(n, p=10, formatar=True):
    resposta = n * (1-(p/100))
    return moeda(resposta) if formatar else resposta


def metade(n, formatar=True):
    if formatar == True:
        return moeda(n / 2)
    else:
        return n / 2


def dobro(n, formatar=True):
    if formatar:
        return moeda(n * 2)
    else:
        return n * 2


def moeda(n):
    res = float(n)
    return f'R${res:.2f}'.replace('.', ',')


def resumo(n, aumenta, diminui):
    print('-' * 30)
    print('RESUMO DA ANÁLISE'.center(30))
    print('-' * 30)
    print('Preço Analisado:'.ljust(20) + moeda(n))
    print('Dobro do Preço:'.ljust(20) + dobro(n))
    print('Metade do Preço:'.ljust(20) + metade(n))
    print(f'{aumenta}% de Aumento:'.ljust(20) + aumentar(n, aumenta))
    print(f'{diminui}% de Redução:'.ljust(20) + diminuir(n, diminui))
    print()
    print('PROGRAMA ENCERRADO'.center(30,'-'))