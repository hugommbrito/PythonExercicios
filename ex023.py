# Faça um programa que peça um número e diga quantas unidades, dezenas e milhares esse número tem.
# Primeira Forma: Como fiz de forma intuitiva
"""num = int(input('Digite um número inteiro até 9999: '))
print('Esse número é composto por:')
mil = int(num / 1000)
print('Milhares: {}'.format(mil))
cem = int(num / 100) - (mil * 10)
print('Centenas: {}'.format(cem))
dez = int(num / 10) - (cem * 10) - (mil * 100)
print('Dezenas:  {}'.format(dez))
uni = num - (dez * 10) - (cem * 100) - (mil * 1000)
print('Unidades: {}'.format(uni))"""

# Segunda Forma: Como ele resolveu no vídeo, usando DIVISÃO INTEIRA (//) e RESTO DA DIVISÃO (% 10)
num = int(input('Digite um número inteiro até 9999: '))
print('\033[1mEsse número é composto por:\033[m')
mil = num // 1000 % 10
print('Milhares: {}'.format(mil))
cem = num // 100 % 10
print('Centenas: {}'.format(cem))
dez = num // 10 % 10
print('Dezenas:  {}'.format(dez))
uni = num // 1 % 10
print('Unidades: {}'.format(uni))
