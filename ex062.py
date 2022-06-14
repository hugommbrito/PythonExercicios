# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print('\033[1;34mCALCULADORA DE PA\033[m')
print('=-'*15)
pt = int(input('Primeiro termo: '))
rz = int(input('Razão da PA: '))
print('=-' * 15)
qt = 10
pa = pt
cont = 0

print(pt, '-> ', end='')
cont += 1
while qt > 1:
    cont += 1
    pa += rz
    print(pa, '-> ', end='')
    qt -= 1
print('PAUSA\n')

nqt = 1
while nqt != 0:
    nqt = int(input('Quantos termos mais você deseja ver? '))
    nc = 0
    while nc < nqt:
        cont += 1
        pa += rz
        print(pa, '-> ', end='')
        nc += 1
    print('PAUSA\n' if nqt != 0 else 'FIM')
print(f'Progressão finalizada com {cont} termos exibidos.')
