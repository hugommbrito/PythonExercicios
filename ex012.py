# Aks for the price of a product and aply a 5% discount.
originalPrice = float(input('What is the price of th product? R$'))
discount = 0.05
discountedPrice = originalPrice * (1-discount)
print(f"Aplying a  {discount*100:.2f}% discount, the product will cost \033[1;32mR${discountedPrice:.2f}\033[m,")
