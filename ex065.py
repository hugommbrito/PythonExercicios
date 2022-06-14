# Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

kg = 'z'  # kg is for Keep Going
num = 0
add = count = big = small = None
while kg != 'n':
    num = int(input('Digite um número: '))
    if count is None:
        add = big = small = num
        count = 1
    else:
        add += num
        count += 1
        if num > big:
            big = num
        if num < small:
            small = num

    kg = str(input('Deseja continuar [S/N]? ')).strip().lower()
    kg = kg[0]
    while kg != 's' and kg != 'n':
        if kg != 's' and kg != 'n':
            print('Opção Inválida! Digite S ou N para continuar ou parar.')
        kg = str(input('Deseja continuar [S/N]? ')).strip().lower()[0]
print(f'\nPrograma Finalizado!!!\nVocê digitou {count} números, a sua média é {add/count}.\nO maior número digitado'
      f'foi {big}, enquanto o menor foi {small}.')
