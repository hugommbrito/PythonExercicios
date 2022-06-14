# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
# sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from datetime import date

nascimento = int(input('Em que ano você nasceu?'))
atual = date.today().year - nascimento

if atual <= 9:
    print(f'Você tem {atual} anos. Sua categoria é MIRIM')
elif atual <= 14:
    print(f'Você tem {atual} anos. Sua categoria é INFANTIL')
elif atual <= 19:
    print(f'Você tem {atual} anos. Sua categoria é JUNIOR')
elif atual <= 25:
    print(f'Você tem {atual} anos. Sua categoria é SENIOR')
else:
    print(f'Você tem {atual} anos. Sua categoria é MASTER')
