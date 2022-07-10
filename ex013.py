# Ask for someones salary and return it's value after a 15% raise.
originalSalarie = float(input('What is your salary?'))
raiseRate = 0.15
raisedSalary = originalSalarie * ( 1 + raiseRate)
print(f'After a \033[1;32m{raiseRate * 100:.0f}%\033[m raise, your salarie will be \033[1;32mR${raisedSalary:.2f}\033[m.'
      f' Much better, right?')
