tempRoom = int(input())
tempTarget = int(input())
if tempRoom == tempTarget:
    power = 0
else:
    if tempRoom < tempTarget:
        power = (tempTarget - tempRoom) * 10
    else:
        power = (tempRoom - tempTarget) * 8
if power > 100:
    power = 100
else:
    power = power
print(power)
