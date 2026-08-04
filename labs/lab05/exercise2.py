import math
radius = input("RADIUS: ")

radius = float(radius)

area = math.pi * (radius * radius)
circumference = (2 * math.pi) * radius

print(f"CIRCLE AREA IS : {area} and ITS CIRCUMFERENCE IS : {circumference}.")