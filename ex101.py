# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


def idade(anoNascimento):
    from datetime import date
    return date.today().year - anoNascimento


def voto(anoNascimento):
    idadeCalc = idade(anoNascimento)
    if idadeCalc < 16:
        return 'NEGADO'
    elif idadeCalc < 18:
        return 'OPCIONAL'
    elif idadeCalc < 65:
        return 'OBRIGATÓRIO'
    else:
        return 'OPCIONAL'


ano = int(input('Em que ano você nasceu?'))
print(f'Você tem {idade(ano)} anos, portanto o voto é {voto(ano)}')
