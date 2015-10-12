import re

myList = [True, False, True, True, False]
print(myList[::-1])

namesList = ["George", "Paul", "Ringo"]
namesList.insert(1, "John")
print(namesList)

numbersList = [2, 3, 5, 7, 11, 13, 15, 17, 19]
numbersList.pop(6)
print(numbersList)
numbersList.insert(6, 15)
numbersList.remove(15)
print(numbersList)

myString = "GOod Morning"
print(myString.lower())

myString = "Title"
print(myString.center(44, " "))

print(numbersList[-1])

myString = "This is a string"
print(myString.split(' '))

myString = "http://www.coventry.ac.uk"
print(myString)
print(re.sub(r'http://', '', myString))
