# Pedir uma número e entregar a sua tabuada.

# Primeira forma: Com os conhecimentos até agora do Curso em Vídeo
cor = {'red': '\033[1;31m',
       'black': '\033[1;30m',
       'green': '\033[1;32m',
       'yellow': '\033[1;33m',
       'blue': '\033[1;34m',
       'purple': '\033[1;35m'}

n = int(input('Digite um número inteiro entre 0 e 9:'))
print('Segue a tabuada para {}:'.format(n))
print('\033[1;30m=-'*10)
print('\033[1;31m', n, 'x 1 = ', n*1)
print(n, 'x 2 = ', n*2)
print(n, 'x 3 = ', n*3)
print(n, 'x 4 = ', n*4)
print(n, 'x 5 = ', n*5)
print(n, 'x 6 = ', n*6)
print(n, 'x 7 = ', n*7)
print(n, 'x 8 = ', n*8)
print(n, 'x 9 = ', n*9)
print('\033[1;30m-='*10)

# Segunda Forma: Como aprendi no curso Python for Everybody

'''n = int(input('Digite um número: '))
print(f'A tabuada para {n} é: ')
for t in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(f'{n} x {t} = {n*t}')
print('=*'*8)'''
