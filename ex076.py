#  Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#  No final, mostre uma listagem de preços, organizando os dados em forma tabular.

# Primeira Forma: Como fiz de maneira intuitiva

"""lista = ('Lápis', '1.75', 'Borracha', '2.00', 'Caderno', '15.00', 'Estojo', '25.00', 'Transferidor', '4.20',
           'Compasso', '9.99', 'Mochila', '120.32', 'Canetas', '22.30', 'Livro', '34.90')

print('-' * 40)
print('LISTGEM DE PREÇOS'.center(40))
print('-' * 40)

for a in range(0, len(lista), 2):
    print(lista[a], '.' * (29-len(lista[a])), f'R${lista[a+1]:>7}')"""

# Segunda Forma: Como ele fez no curso

lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.00, 'Estojo', 25.00, 'Transferidor', 4.20,
           'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-' * 40)
print(f'{"LISTGEM DE PREÇOS":^40}')
print('-' * 40)

for a in range(0, len(lista)):
    if a % 2 == 0:
        print(f'{lista[a]:-<30}', end='')
    else:
        print(f'R${lista[a]:>7}')

print('-' * 40)