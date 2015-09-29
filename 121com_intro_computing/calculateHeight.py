from __future__ import division
heightFeet = input("Enter your height - feet: ")
heightInches = input("Inches: ")
def calculateInches(feet, inches):
    return (feet * 12) + inches
totalInches  = calculateInches(heightFeet, heightInches)
print((totalInches / 12) * 0.3)
