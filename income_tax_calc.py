income = float(input('Enter the income: '))

income_tax = 0
if income_tax > 5_00_000 and income < 10_00_000:
    income_tax = income * (5/100)
elif income_tax >= 10_00_000 and income < 20_00_000:
    income_tax = income * (10/100)
else:
    income_tax = 0

print(f'Tax on {income} is {income_tax}')