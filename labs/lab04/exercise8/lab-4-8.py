distance = int(input())
afterMidnight = input()
if distance > 2:
    fare = 4.0 + distance - 2 * 1.2
else:
    fare = 4.0
if afterMidnight == "yes":
    fare = fare + 3.0
else:
    fare = fare
print(fare)
