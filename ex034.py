# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salary_limit = 1250
lower_sal_raise = 1.15
upper_sal_raise = 1.10

salary = float(input('Qual é o seu salário? '))

if salary <= salary_limit:
    new_salary = salary * lower_sal_raise
    print('Você receberá um aumento de \033[32m{:.0f}%\033[m e ficará com um salário de \033[32mR${:.2f}\033[m'
          .format(((lower_sal_raise - 1)*100), new_salary))
else:
    new_salary = salary * upper_sal_raise
    print('Você receberá um aumento de \033[34m{:.0f}%\033[m e ficará com um salário de \033[34mR${:.2f}\033[m'
          .format(((upper_sal_raise - 1)*100), new_salary))
