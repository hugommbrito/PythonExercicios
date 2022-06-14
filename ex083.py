# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

# Como resolvi de forma intuitiva
"""expressao = input('Digite uma expressão matemática: ')
testeDaExpressao = 0

for i in expressao:
    if i == '(':
        testeDaExpressao += 1
    elif i == ')':
        testeDaExpressao -= 1

    if testeDaExpressao < 0:
        print('Expressão Inválida, você fechou parênteses que não foram abertos.')
        break

if testeDaExpressao == 0:
    print('Expresão validada com Sucesso.')
elif testeDaExpressao > 0:
    print('Expressão Inválida, faltou fechar algum parêntese.')"""

# Como ele resolveu no vídeo
expr = str(input('Digite a expressão: '))
pilha = []

for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está válida.')
else:
    print('Expressão Inválida.')
