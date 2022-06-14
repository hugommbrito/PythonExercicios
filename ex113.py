# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da
# digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.


# Como eu fiz
"""def leiaInt(msg):
    while True:
        num = input(msg).strip()
        try:
            nInt = int(num)
            return nInt

        except:
            print(f'\033[31m"{num}" não é um número inteiro, tente novamente.\033[m')


def leiaFloat(msg):
    while True:
        num = input(msg).strip()
        try:
            float(num)
            return float(num)

        except ValueError:
            print(f'\033[34m"{num}" não é um número real, tente novamente.\033[m')"""

# como ele fez
def leiaInt(msg):
    while True:
        num = input(msg).strip()
        try:
            nInt = int(num)

        except (ValueError, TypeError):
            print(f'\033[31m"{num}" não é um número inteiro, tente novamente.\033[m')

        else:
            return nInt


def leiaFloat(msg):
    while True:
        num = input(msg).strip()
        try:
            float(num)

        except (ValueError, TypeError):
            print(f'\033[34m"{num}" não é um número real, tente novamente.\033[m')

        else:
            return float(num)


# Programa Principal
n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'Você digitou o número inteiro {n1} e o número real {n2}')
