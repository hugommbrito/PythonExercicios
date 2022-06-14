# Peça o valor do salário e mostre qual será o novo valor após um aumento de 15%
s = float(input('Qual o seu salário atual?'))
a = 0.15
ns = s*(1+a)
print('Após um aumento de \033[1;32m{:.0f}%\033[m o seu salário será de \033[1;32mR${:.2f}\033[m. Bem melhor, hein?'
      .format((a*100), ns))
