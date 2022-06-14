#  Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
#  o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário
#  ou então o empréstimo será negado.

house = float(input('Quanto custa a casa que você quer comprar? '))
salary = float(input('Quanto é o seu salário? '))
years = float(input('Em quantos anos você pretende dividir o valor?'))

installments = house / (years * 12)

if installments <= (salary * 0.3):
    print('\033[1;32mParabéns, o seu empréstimo foi aprovado.\033[m')
else:
    print('\033[1;31mInfelizmente o seu empréstimo foi negado\033[m\n'
          '\033[1;33mComo sugestão, você pode procurar uma casa mais barata ou parcela-la em mais tempo.')
