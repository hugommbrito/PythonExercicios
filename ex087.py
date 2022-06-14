# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0

for l in range(0, 3):
    for c in range(0, 3):
        num = int(input(f'Digite um número para a posição [{l}, {c}]:'))
        matriz[l][c] = num
        if num % 2 == 0:
            pares += num

print("-=" * 22)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print("-=" * 22)
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')