gb = float(input())
planA = 10 + (gb * 1)
if gb > 20:
    planB = ((gb - 20) * 3) + 25
else:
    planB = 25
if planA > planB:
    bill = planB
else:
    bill = planA
print(bill)
