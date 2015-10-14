# Fix this buggy code
options = ["Eat an Apple", "World Peace", "Destroy the World"]
print("Here are your options:")
count=1
for opt in options:
    print(str(count) + ". " + opt)
    count=count+1
x = int( input("What would you like to do? ") )
print("Ok... " + options[x - 1]) #Here is the logic error, due to misunderstanding of indexing

# Note: It's a silly example, but a serious point.
# Such logic erros can be really hard to find and have big consequences!
