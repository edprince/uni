sentence = input("Please enter a sentence")
#Boo
myList = sentence.split(" ")
mySet = set(myList)
print(myList)
myDictionary = {}
uniqueWords = []

def word_frequency(x):
    count = 1
    for i in x:
        print(i)
        if (i in uniqueWords):
            count += 1
            myDictionary[i] = count
        else:
            uniqueWords.append(i)
            myDictionary[i] = 1
        print(uniqueWords)
    return myDictionary
print(word_frequency(myList))
