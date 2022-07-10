# Ask for hom many days will someone rent a car and how many km will they run on it, then calculate the rental price
# use R$60,00/day and R$0,15/km
days = int(input('How many days will you be with the car?'))
km = float(input('How many Kilometers will you drive with it?'))
pricePerDay = 60
pricePerKm = 0.15
rentalPrice = (days * pricePerDay) + (km * pricePerKm)
print(f'\033[4;30;41mThe rental will cost R${rentalPrice:.2f}.\033[m')
