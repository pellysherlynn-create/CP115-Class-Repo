principal = float(input())
rate = float(input())
time = float(input())
interest = principal * rate / 100 * time
totalAmount = principal + interest
monthlyInterest = interest / time * 12
print(interest)
print(totalAmount)
print(monthlyInterest)
