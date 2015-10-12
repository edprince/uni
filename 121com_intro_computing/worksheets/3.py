import math
print(math.log(1234, 10))
print(math.e**2)
print(math.pi / 2)
print(math.cos(math.pi / 2))
print((math.sin(math.pi / 4))**2)
print(math.asin(1))

print("+" + "-" * 50 + "+")

myList = [1, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10]

def calculateMean(x):
    i = 0
    currentTotal = 0
    for i in x:
       currentTotal += x[i]
       i += 1
    return currentTotal / i

def calculateMedian(x):
    length = len(x)
    print("Length - " + str(length))
    if length % 2 != 0:
        return x[math.floor(length / 2)]
    else:
        array = [x[length / 2], x[length / 2]]
        return calculateMean(array)

print(calculateMean(myList))
print(calculateMedian(myList))
