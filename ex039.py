# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda
# vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano1 = int(input('\033[1mEm que ano você nasceu?\033[m'))
ano2 = date.today().year

if ano2 - ano1 == 18:
    print('\033[1;34mProcure o quartel mais próximo, você deve se alistar esse ano.')
elif ano2 - ano1 > 18:
    print('\033[1;31m Você já deveria ter se alistado.')
else:
    print('\033[1;32mNão se preocupe, você ainda não precisa se alistar.')
