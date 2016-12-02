'''PSEUDOCODE
INPUT some_string
SPLIT some_string INTO list_of_words
REVERSE list_of_words
CONCATENATE list_of_words INTO STRING
'''
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

myString = raw_input('enter something: ')
print(reverseOrder(myString))
