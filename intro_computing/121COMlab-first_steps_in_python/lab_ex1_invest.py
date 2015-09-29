def whichBank(investment, percentage, years):
    return investment * ((1 + (percentage / 100))**years)

print 10000 * (1 + (1 / 100))**5
valueA = whichBank(10000, 1, 3)
valueA = valueA + whichBank(valueA, 5 ,2)

valueB = whichBank(10000, 1, 4)
valueB = valueB + whichBank(valueB, 10, 1)

valueC = whichBank(10000, 2, 5)


print(str(valueA) + " - Bank A")
print(str(valueB) + " - Bank B")
print(str(valueC) + " - Bank C")
