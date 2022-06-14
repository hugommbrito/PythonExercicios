# Peça um número e entregue o seu dobro, seu triplo e sua raiz quadrada.
n = float(input('\033[1;34mDigite um número:\033[m'))
d = n*2
t = n*3
r2 = n**(1/2)
print('Você digitou o número {:.0f},\n se dobrado ele vira {:.0f},\n se triplicado vira {:.0f},\n mas a sua raiz '
      'quadrada é {:.2f}.'.format(n, d, t, r2))
