# Escreva um código que peça um ângulo e escreva qual o seu Seno, Cosseno e a Tangente

# Primeira forma: importando a biblioteca math completa e com um print() para cada dado.
"""import math
angulo = int(input('Digite um ângulo: '))
sen = math.sin(math.radians(angulo))
print('O Seno de {}º é {:.2f}'.format(angulo, sen))
cos = math.cos(math.radians(angulo))
print('O Cosseno de {}º é {:.2f}.'.format(angulo, cos))
tan = math.tan(math.radians(angulo))
print('A Tangnte de {}º é {:.2f}.'.format(angulo, tan))"""

# Segunda forma: importando apenas as fórmulas necessárias da biblioteca math e colocando tudo em um print() só.
from math import sin, cos, tan, radians
a = int(input('Digite um ângulo:'))
sen = sin(radians(a))
cos = cos(radians(a))
tan = tan(radians(a))
print('\033[7mO Seno de {} é {:.2f} \n O Cosseno de {} é {:.2f} \n A Tangente de {} é {:.2f}'
      .format(a, sen, a, cos, a, tan))
