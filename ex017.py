# Desenvolva um programa que pegue o tamanho de doi catetos e calcule o tamanho da hipotenusa.

# Primeira forma: Calculando com pelos quadrados (**)
"""co = int(input('Digite o tamanho do Cateto Oposto: '))
ca = int(input('Digite o tamanho do Cateto Adjacente: '))
h = ((co**2)+(ca**2))**(1/2)
print('Para um triangulo com catetos medindo {} e {}, a hipotenusa vai medir {:.2f}.'.format(co, ca, h))"""

# Segunda forma: Calculando pela formula pow()
"""co = float(input('Qual o tamanho do Cateto Oposto? '))
ca = float(input('Qual o tamanho do Cateto Adjacente? '))
h = pow(pow(co,2) + pow(ca,2),0.5)
print('Para um triângulo com catetos de {} e {}, a hipotenusa é {:.2f}.'.format(co, ca, h))"""

# Terceira forma: Usando a fórmula hypot() da biblioteca .math
from math import hypot
co = int(input('Digite o Cateto Oposto: '))
ca = int(input('Digite o Cateto Adjacente: '))
h = hypot(co, ca)
print('\033[1;33mPara um triângulo com catetos de {} e {}, a hipotenusa é {:.2f}.'.format(co, ca, h))
