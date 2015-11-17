global file_object
file_object = open('ackermann_result.txt', 'w')

def ackermann(m, n, count):
    global file_object
    file_object.write('Hello \n')
    count += 1
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ackermann(m - 1, 1, count)
    if m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1, count), count)
    return count

print(ackermann(2, 2, 0))

def ackermann_efficient(m, n, count, d):
    print('Hello')
    count += 1
    if d[(m, n)] != '':
        pass 
    else:
        #d[(m, n)] = 
        if m == 0:
            return n + 1
        if m > 0 and n == 0:
            return ackermann_efficient(m - 1, 1, count)
        if m > 0 and n > 0:
            return ackermann_efficient(m - 1, ackermann_efficient(m, n - 1, count), count)
    return count

#print(ackermann_efficient(3, 4, 0))

dictionary = {(4, 1): 4}

