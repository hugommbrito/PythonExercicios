# Pedir uma medida em metros e converte-la para centimetro e milímetros.
n = float(input('Digite a medida em metros:'))
cm = n*100
mm = n*1000
print('Você digitou \033[7m{:.2f}m\033[m, que podem ser convertidos em \033[1;34m{:.0f}cm\033[m ou '
      '\033[1;36m{:.0f}mm\033[m'.format(n, cm, mm))
