minutesBefore = int(input())
membership = input()
if minutesBefore < 0:
    price = 0
else:
    if minutesBefore > 30:
        price = 80 - 15
    else:
        price = 80
if membership == "yes":
    price = price * 0.85
else:
    price = price
print(price)
