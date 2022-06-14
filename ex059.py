# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
n1 = int(input('Digite o primerio valor: '))
n2 = int(input('Digite o segundo valor: '))

cor = {'negr': '\033[1m', 'fim': '\033[m'}
opção = 0
maior = 0
while opção != 5:
    print('\n')
    print('=*'*20)
    print('Escolha o que você deseja fazer.')
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Ver o Maior')
    print('[ 4 ] Escolher novos números')
    print('[ 5 ] Sair do programa')
    opção = int(input('Digite a opção escolhida:'))
    if opção == 1:
        print(f"{cor['negr']}A soma etre {n1} e {n2} é {n1+n2}.{cor['fim']}")

    elif opção == 2:
        print(f"{cor['negr']}{n1} vezes {n2} é {n1*n2}{cor['fim']}")

    elif opção == 3:
        if n1 > n2:
            print(f"{cor['negr']}{n1} é maior do que {n2}.{cor['fim']}")
        elif n1 < n2:
            print(f"{cor['negr']}{n2} é maior do que {n1}.{cor['fim']}")
        elif n1 == n2:
            print(f"{cor['negr']}Os números são iguais{cor['fim']}")

    elif opção == 4:
        print('\n')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))

    elif opção == 5:
        print(f"{cor['negr']}PROGRAMA ENCERRADO COM SUCESSO!{cor['fim']}")

    else:
        print(f"{cor['negr']}Opção invélida, digite uma das opções abaixo.{cor['fim']}")
    sleep(2)
