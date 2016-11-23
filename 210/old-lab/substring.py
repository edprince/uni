def substring(s, b, l):
    return s[0:b] + s[b+l:len(s)]

userString = raw_input('Please enter a string: ')
startSplice = int(input('Please enter the index of start of substring: '))
spliceLength = int(input('Enter the length of the splice sub: '))
print(substring(userString, startSplice, spliceLength))

