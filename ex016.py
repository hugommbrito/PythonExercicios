# Faça um programa que pegue um número e diga qual a sua porção inteira.

# Primeira forma, importando biblioteca math completa
import math
n = float(input('v1 Digite um número: '))
nint = math.trunc(n)
print(f'\033[1mA parte inteira do número {n} é {nint}.')

# Segunda forma, importando apenas a função trunc na biblioteca math
'''from math import trunc
n = float(input('v2 Digite um número: '))
ni = trunc(n)
print('A porção inteira do número {} é {}.'.format(n, ni))'''

# Terceira Forma, usando a formula de arredondar para baixo
'''from math import floor
n = float(input('v3 Digite um número: '))
nf = floor(n)
print('Arredondando para baixo, a parte inteira de {} também é {}'.format(n, nf))'''
