import string

#sentence = open('asoiaf.txt', 'r').read().lower()
sentence = input("Please enter a sentence: ").lower()
myList = sentence.split(" ")
sortedList = sorted(myList)
print(sortedList)

i = 0 
u = 0 
totalOccurences = 0
letterOccurences = []

mySet = list(set(sortedList))
print(mySet)

for i in range(0, (len(sortedList))):
    letterOccurences.append(sortedList.count(sortedList[i]))

print("Word | Occurences")
for i in range(0, (len(sortedList))):
    print(mySet[i] + " | " + str((letterOccurences[i])))
