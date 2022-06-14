# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram
# no intervalo de 1 até 500.
soma = 0
conta = 0
for n in range(0, 500, 3):
    if n % 2 != 0:
        conta = conta + 1
        soma = soma + n
print(f'Após somar {conta} números que correspondem aos requisitos, obtemos o resultado de {soma}')
