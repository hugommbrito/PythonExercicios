# Escreva um programa que pergunte a distância de uma viagem e calcule considerando R$0,50/km para viagens até 200km e
# R$0,45/km para viagens acima de 200km.

# Primeira forma: usando IF comum
trip_len = float(input('Qual a distância de sua viagem? '))
price_short = 0.50
price_long = 0.45

if trip_len <= 200:
    price = trip_len * price_short
    print('\033[1;33m Sua passagem custará R${:.2f}\033[m'.format(price))
else:
    price = trip_len * price_long
    print('\033[1;34m Sua passagem custará R${:.2f}\033[m' .format(price))

# Segunda forma: Usando o IF simplificado
"""trip_len = float(input('Qual a distância da sua viagem? '))
price_short = 0.50
price_long = 0.45

price = trip_len * price_short if trip_len <= 200 else trip_len * price_long

print('\033[1;36mSua passagem custará R${:.2f}.\033[m'.format(price))"""
