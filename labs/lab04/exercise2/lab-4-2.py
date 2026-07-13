income = int(input())
if income >= 50000:
    if income >= 100000:
        totalTax = (50000 * 0.01) + ((income - 100000) * 0.02)
    else:
        totalTax = (income - 50000) * 0.01
else:
    totalTax = (income * 0.0)
print(totalTax)
