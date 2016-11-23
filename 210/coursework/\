def reverseOrder(userString):
    '''Function to reverse the order of words in a string

    Takes any valid sentence and reverses the word order'''
    wordList = userString.split(' ')
    reversedList = wordList[::-1]
    newString = ''
    for x in range(len(reversedList)):
        if x == 0:
            newString += reversedList[x]
        else:
            newString += ' ' + reversedList[x]
    return newString

print(reverseOrder(
input('Please enter your string: ')
))
