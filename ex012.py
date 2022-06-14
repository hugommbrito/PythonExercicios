# Pedir o preço de um produto e aplicar um desconto de 5%
p = float(input('Qual o valor do produto? R$'))
d = 0.05
pd = p * (1-d)
print("Aplicando o desconto de {:.2f}%, o produto ficará por \033[1;32mR${:.2f}\033[m,".format((d*100), pd))
