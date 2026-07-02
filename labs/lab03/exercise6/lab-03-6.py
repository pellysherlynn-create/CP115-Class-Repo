yardLength = float(input())
yardWidth = float(input())
houseLength = float(input())
houseWidth = float(input())
houseArea = yardLength * yardWidth
builtInhouseArea = houseLength * houseWidth
yardArea = houseArea - builtInhouseArea
wage = yardArea * 2.0
print(wage)
