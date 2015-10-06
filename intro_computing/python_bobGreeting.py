from __future__import print_function

try:
  input = raw_input
except NameError:
  pass

from datetime import date

year = input("What year were you born?")
noOfYears = date.today().year - int(year)

print("You have been alive for ", noOfYears * 7, " dog years!")
