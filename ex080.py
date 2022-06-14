# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela


# Esse desafio eu só consegui resolver visualizando a resposta.
lista = []
for a in range(0, 5):
    num = int(input('Digite um número: '))
    if lista == [] or num > lista[-1]:  # Checa se o número inserido é o 1º a ser inserido ou se é maior que o último.
        lista.append(num)
    else:  # Encontra o espaço correto para inserir o número
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1

print('+-' * 30)
print(f'Os valores digitados em ordem foram {lista}')
