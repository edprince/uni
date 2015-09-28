from datetime import date
year = input("What year were you born?")
noOfYears = date.today().year - year
print("You have been alive for ", noOfYears * 7, " dog years!")
