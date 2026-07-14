kwh = int(input())
if kwh <= 100:
    totalBill = kwh * 0.3
else:
    if kwh <= 200:
        totalBill = kwh * 0.5
    else:
        totalBill = kwh * 0.25
print(totalBill)
