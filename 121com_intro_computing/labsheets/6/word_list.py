words = open('words.txt', 'r')
words = [s.strip() for s in words.splitlines()]

def is_this_a_word(s):
    for x in range(len(words) - 1):
        if words[x].lower() == s:
            return True

#is_this_a_word('true')
