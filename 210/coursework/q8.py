'''PSEUDOCODE
INPUT userString
IF userString EQUALS 0 THEN
  RETURN userString
ELSE IF first letter IS VOWEL THEN
  CALL REMOVEVOWEL ON userString MINUS first letter
ELSE
  RETURN first letter ADD REMOVEVOWELS ON userString MINUS first letter
'''
def removeVowels(userString):
    if len(userString) == 0:
        return userString
    elif userString[0] in 'aAeEiIoOuU':
        return removeVowels(userString[1:])
    return userString[0] + removeVowels(userString[1:])

print(removeVowels('beautiful trees'))
    
    
