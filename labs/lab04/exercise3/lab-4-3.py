hours = int(input())
if hours >= 2:
    if hours >= 5:
        parkingFee = 0 + ((hours - 2) * 2.0) + ((hours - 5) * 3.0)
        if parkingFee >= 30:
            parkingFee = 30.0
        else:
            parkingFee = parkingFee
    else:
        parkingFee = 0 + ((hours - 2 ) * 2.0)
else:
    parkingFee = (0.0)
print(parkingFee)
