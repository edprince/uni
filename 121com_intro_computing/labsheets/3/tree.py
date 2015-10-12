import math
width = 0
length = 3
while ((width + length) % 2) != 0:
    length = int(input("Please enter the height of your tree: "))
    width = int(input("Please enter the width of your tree: "))
i = 0 
for i in range(1, width + 1, 2):
    print(" " * math.floor(width - (i) / 2) + "*" * i)

for i in range(1, length + 1):
    print(" " * math.floor((width - 1) / 2) + " " * math.floor((width - 2) / 2) + "*" * 3 + " " * 3)



