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
