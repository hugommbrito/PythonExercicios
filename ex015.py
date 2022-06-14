# Pergunte quantos km foram percorridos por um carro e por quantos dias foi alugado e calcule o preço do aluguel
# (60/dia e 0.15/km)
dias = int(input('Quantos dias você ficou com o carro?'))
km = float(input('Quantos km você rodou com o carro?'))
pdia = 60
pkm = 0.15
aluguel = (dias * pdia) + (km * pkm)
print('\033[4;30;41mO valor total da locação é de R${:.2f}.\033[m'.format(aluguel))
