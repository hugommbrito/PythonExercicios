# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
print('-'*20, '\nPROGRAMA DA TABUADA\n', '-'*20)

while True:
    t = int(input('\nDe qual número você quer ver a tabuada? '))
    if t < 0:
        break

    print('*'*13)
    for c in range(1, 11):
        print(f'{t} x {c:>2} = {c * t:>2}')
    print('*' * 13)
print('PROGRAMA ENCERRADO!')
