# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos
# de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

print('-='*15, '\nSequência de Fibonacci\n', '=-'*14)
q = int(input('\nQuantos termos você quer mostrar? '))

n0 = 0
n1 = 1

print(f'{n0} -> {n1} -> ', end='')
while (q-2) > 0:
    sf = n0 + n1
    print(sf, '-> ', end='')
    n0 = n1
    n1 = sf
    q -= 1
print('FIM')
