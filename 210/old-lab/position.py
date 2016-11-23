cont = True
userList = []
while cont == True:
    val = input('Please enter a number (q to stop): ')
    if (val == 'q'):
        cont = False
    else:
        userList.append(int(val))

tmp_largest = userList[0];
tmp_smallest = userList[0];
smallest_position = 1;
largest_position = 1;

for i in range(1, len(userList)):
    if (userList[i] > tmp_largest):
        tmp_largest = userList[i]
        largest_position = i + 1
    elif (userList[i] < tmp_smallest):
        tmp_smallest = userList[i]
        smallest_position = i + 1

print('Largest: ', tmp_largest, ' at position: ', largest_position)
print('Smallest: ', tmp_smallest,' at position: ', smallest_position)
