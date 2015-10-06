# Script for working with daily currency data provided by ECB.

# url for ECM data in xml format
url = "http://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml"
#1 XDR = 0.423 Euros + 12.1 Japanese Yen + 0.111 British Pounds + 0.66 US Dollars

#####################################################################
# In this block of code:
# - Python opens the url
# - reads the data
# - stores it as a string
# - closes the url
import urllib.request
page = urllib.request.urlopen(url)
data_bytes = page.read()
data_string = data_bytes.decode('utf-8')
page.close()
#####################################################################

#####################################################################
# In this block of code:
# - Python converts the string into an element tree
# - Extracts  the data and create variables:
# Each variable name is a currency code and each
#   value is the rate for 1 euro.
import xml.etree.ElementTree as ET
data_tree = ET.fromstring(data_string)
for child in data_tree[2][0]:
    countryD = child.attrib
    exec("%s = %f" % (countryD["currency"], float(countryD["rate"])))
# Note: there is a much better way for Python to handle such data
#   (called a dictionary) but we havn't met that yet. 
#####################################################################

#####################################################################
#Example:
print("One euro is " + str(GBP) + "GBP (Great British Pounds)")
print("+" + ("-" * 48) + "+")
print("Five hundred EUR is " + str(USD * 500) + " USD (United States Dollars)")
print("Two hundred GBP is " + str(((1 / GBP) * 200) * CNY) + " CNY (Chinese Yuan)")
print("One thousand RUB is " + str(((1 / RUB) * 1000) * INR) + " INR (Indian Rupee)")
print("+" + ("-" * 48) + "+")
XDREuro = (0.4323 + (1 / (JPY / 12.1)) + (1 / (GBP / 0.111)) + (1 / (USD / 0.66)))
XDR
print("XDR: " + str(XDR) + " EUR")
#####################################################################
