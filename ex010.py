# Ask how much money does someone have and convert it to American Dolars (1USD = 3.27BRL)
amount = float(input('How much money have you got in your wallet? R$'))
exchangeRate = 3.27
convertion = amount/exchangeRate
print(f"You've got \033[1;32mR${amount:.2f}\033[m in your wallet. Considering the Exchange rate of R${exchangeRate:.2f} "
      f"for each dolar, you can buy \033[1;32mUSD{convertion:.2f}\033[m!")
