import string
sentence = input("Please enter a sentence: ").lower()
myList = sentence.split(" ")
sortedList = sorted(myList)
print(sortedList)
