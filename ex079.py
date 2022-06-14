# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Cso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente.

conti = 't'
lista = []
while True:
    print('-' * 40)
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
        print(f'Número {n} adicionado com sucesso')
    else:
        print(f'Número {n} já foi adicionado, não irei adicionar novamente.')

    conti = str(input('Deseja cotiuar? [S/N] ')).strip()[0]
    if conti in 'Nn':
        break

print('=-' * 20)
print(f'Você digitou os números {sorted(lista)}')
