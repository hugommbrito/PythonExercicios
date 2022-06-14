# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

n1 = float(input('Primeira Nota:'))
n2 = float(input('Segunda Nota:'))

media = (n1+n2)/2

if media < 5:
    print('\033[1;31mVocê foi REPROVADO, tente se dedicar mais no ano que vem.\033[m')
elif 5 <= media < 7:
    print('\033[1;33mVocê está na RECUPERAÇÃO, ainda da para recuperar o esforço desse ano.\033[m')
elif media >= 7:
    print('\033[1;32mParabéns, você está APROVADO! Ano que vem nos vemos com novos desafios!\033[m')
