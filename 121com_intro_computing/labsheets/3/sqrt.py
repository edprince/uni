import math

#q5
difference = 1
loop = True
x = int(input("Please enter a value for x: "))
y = (x + 1) / 2


iterations = 1

while loop == True:
    if y**2 - x < 0.001:
        loop = False
    else:
        y = (y + x / y) / 2
        iterations += 1
        if y**2 - x < 0.001:
            loop = False

print(y)
print(str(iterations) + " loops were needed")
print("Math sqrt - " + str(math.sqrt(x)))

