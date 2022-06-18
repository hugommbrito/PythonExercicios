# Ask for a number and then deliver a mensage with the previous and the following numbers.
number = int(input('Type a integere number:'))
print(
    f"You've typed \033[1m{number}\033[m, it's predecessor is \033[1;35m{(number - 1)}\033[m and it's successor is"
    f" \033[1;36m{(number + 1)}\033[m")
