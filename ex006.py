# ask for a number and than deliver it's double, it's triple and the square root.
number = float(input('\033[1;34mType a number:\033[m'))
double = number * 2
triple = number * 3
sqRoot = number ** (1 / 2)
print(f'You have typed the number {number:.0f},\n if doubled it becomes {double:.0f},\n if tripled it becomes'
      f' {triple:.0f},\n but the square root is {sqRoot:.2f}.')
