# Escreva um programa que peça três números e depois diga qual o maior e qual o menor deles.
# Primeira forma: Fazendo só e tentando fazer diferente do que vi no curso Python For Everybody
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Só mais um: '))

colors = {'red': '\033[31m',
          'green': '\033[32m',
          'end': '\033[m'}
if n1 > n2 and n1 > n3:
    print('O maior número é {}{}{}'.format(colors['red'], n1, colors['end']))
elif n2 > n1 and n2 > n3:
    print('O maior número é {}{}{}'.format(colors['red'], n2, colors['end']))
elif n3 > n1 and n3 > n2:
    print('O maior número é {}{}{}'.format(colors['red'], n3, colors['end']))

if n1 < n2 and n1 < n3:
    print('O menor número é {}{}'.format(colors['green'], n1))
elif n2 < n1 and n2 < n3:
    print('O Menor número é {}{}'.format(colors['green'], n2))
elif n3 < n1 and n3 < n2:
    print('O menor número é {}{}'.format(colors['green'], n3))
