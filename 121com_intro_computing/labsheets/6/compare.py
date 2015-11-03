def compare_text(file1, file2):
    myList = open(file1, 'r').readlines()
    myList2 = open(file2,'r').readlines()
    for x in range(len(myList) - 1):
        if myList[x] != myList2[x]:
            for n in range(len(myList[x]) - 1):
                if myList[x][n] != myList2[x][n]:
                    return (x + 1, n + 1)
    return "The files are the same"
                    
print('difference at line, column' + str(compare_text('word_frequency.py',
'word_frequency_copy.py')))
