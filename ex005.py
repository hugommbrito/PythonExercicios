# Pedir um número e entregar uma mensagem com o seu sucessor e antecessor.
n = int(input('Digite um número inteiro:'))
print(
    f'Você digitou \033[1m{n}\033[m, o seu antecessor é \033[1;35m{(n - 1)}\033[m e o seu sucessor é'
    f'\033[1;36m{(n + 1)}\033[m')

# Na revisão da aula vi que é melhor colocar a variável entre parenteses dentro do format.
# Na revisão por cores, a string ficou muito grande e o PyCharm sugeriu fazer a formatação automática para uma f-string
