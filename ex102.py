# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a
# calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado
# ou não na tela o processo de cálculo do fatorial.

def fatorial(n, show=False):
    """
    A função fatorial() calcula, imprime na tela e retorna o fatorial de uma váriavel n
    :param n: Variável que terá seu fatorial calculado
    :param show: Determina se o calculo executado será impresso na tela ou não
    :return: retorna o resultado fatorial de um número n
    """
    result = 1
    for c in range(n, 0, -1):
        result *= c

    if show == True:
        print('-' * 20)
        for c in range(n, 1, -1):
            print(f'{c} x ', end='')
        print(f'1 = {result}')
    else:
        print('-' * 20)
        print(result)

    return result


fatorial(5, show=True)
help(fatorial)