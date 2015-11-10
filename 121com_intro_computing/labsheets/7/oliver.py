oliver_txt = open('oliver.txt', 'r').read()
oliver_list = oliver_txt.split(' ')

dictionary = {}

for i in range(len(oliver_list) - 1):
    dictionary.setdefault(oliver_list[i], [])
    dictionary[oliver_list[i]].append(oliver_list[i + 1])

print(dictionary)


