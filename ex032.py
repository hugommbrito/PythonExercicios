# Crie um programa que pergunte um ano e diga se ele é bissexto ou não.
# Para identificar um ano bissexto, ele deve ser divisível por 4, não pode ser divisível por 100 com excessão dos
# divisíveis por 400.

from datetime import date

year = int(input('Digite um ano, utilize o número 0 para o ano atual: '))

if year == 0:
    year = date.today().year

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('O ano {} é \033[1;44m BISSEXTO \033[m.'.format(year))
else:
    print('O ano {} \033[1;43m NÃO É BISSEXTO '
          '\033[m.'.format(year))
