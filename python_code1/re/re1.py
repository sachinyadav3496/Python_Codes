import re
line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)
if matchObj:
    print("matchObj.group() :",matchObj.group())
    print("matchObj.group(1):",matchObj.group(1))
    print("matchObj.group(2):",matchObj.group(2))
else:
    print("No match!!")
phone = "2004-959-559 # This is Phone Number"
# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print("Phone Num : ", num)
#Remove anything other than digits
num =  re.sub(r'\D', "", phone)
print("Phone Num : ", num)

line = 'Cats are smarter than dogs'
matchObj = re.match(r'dogs', line, re.M|re.I)
if matchObj:
    print("match --> matchObj.group(): ", matchObj.group())
else:
    print("No match!!")
searchObj = re.search(r'dogs', line, re.M|re.I)
if searchObj:
    print("search-->searchObj.group() : ", searchObj.group())
else:
    print("No match!!")
