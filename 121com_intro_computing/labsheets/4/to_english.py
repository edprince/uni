proceed = False
while proceed == False:
    number = input("Please enter a number between 1 and 9999: ")
    if int(number) >= 1 and int(number) <= 9999:
        proceed = True

def convert(x):
    digits = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
    'Eight', 'Nine']
    extensions = ['Hundred', 'Thousand']
    tens = ['teen', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty',
    'Seventy', 'Eighty', 'Ninety']
    place1 = ''
    place2 = ''
    place3 = ''
    place4 = ''
        #Use the digits only
    place1 = calculate_digits(len(int(x) - 1))
    if len(x) == 2:
        #Use digits and tens[0]
        print(x)
    elif int(x) < 30:
        print("This is 20")
        #Use tens[1] and digits
    elif int(x) < 40:
        print("This is 30")
        #Use tens[1] and digits
    elif int(x) < 50:
        #Use tens[1] and digits
        print("This is 40")
    elif len(str(x)) == 4:
        place1 = digits[int(str(x[0])) - 1] +  ' ' + extensions[1]
        for i in range(0, 10):
            if int(x[2]) == (i):
                place3 = tens[i]
            if int(x[len(x) - 1]) == (i + 1):
                place4 = digits[i]
            if int(x[1]) == 0:
                place2 = ' and '
        place2 = digits[int(x[1]) - 1] + ' ' + extensions[0]
        return place1 + ' ' + place2 + ' and ' + place3 + ' ' + place4
print(convert(number))

def calculate_digits(x):
    return digits[int(x) - 1]

def calculate_tens(x):
    return tens(int(x))

def calculate_hundreds(x):
    print(x)


