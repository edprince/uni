def code_only(file):
    with open(file) as f:
        for line in f:
            myString = line
            if myString[0] != '#':
                print(line)

code_only('word_frequency.py')
