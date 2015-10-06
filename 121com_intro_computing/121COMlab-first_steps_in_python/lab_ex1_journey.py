distanceMiles = 4
speedMph = 25
timeAtStop = 120
noOfStops = 10

def calculateTime(speed, distance):
    time = (distance / speed)
    return time

busTime = calculateTime(speedMph, distanceMiles) + timeAtStop * noOfStops
runTime = calculateTime(7, 1)
runTime = runTime + calculateTime(12, 2)
runTime = runTime + calculateTime(7, 1)

print(str(busTime) + " - bus time")
print(str(runTime) + " - run time")
