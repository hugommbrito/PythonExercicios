def aumentar(n, p=10):
    return n * (1+(p/100))


def diminuir(n, p=10):
    return n * (1-(p/100))


def metade(n):
    return n / 2


def dobro(n):
    return n * 2


def moeda(n):
    res = float(n)
    return f'R${res:.2f}'.replace('.', ',')
