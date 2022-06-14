# Faça um programa que peça a velocidade de um carro e diga se ele foi multado ou não, caso ele esteja dirigndo acima de
# 80Km/h calcule a multa para R$7,00 para cada km/h acima do limite de velocidade.

speed = float(input('Qual a Velocidade do carro? '))
sp_limit = 80
fine = 7
calc_fine = (speed - sp_limit) * fine

if speed <= sp_limit:
    print('\033[1;34mParabéns pela direção prudente!')
else:
    print('\033[1;31;40mMULTADO! O limite de velocidade nessa via é de {}Km/h. Você receberá por email uma multa no'
          ' valor de R${:.2f}\033[m'.format(sp_limit, calc_fine))
    print('Dirija com prudência!')
