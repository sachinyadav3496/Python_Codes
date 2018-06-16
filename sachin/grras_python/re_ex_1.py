#!/usr/bin/python
import re
line = "cats are smarter than dogs "
matchObj = re.match(r'(.*) are(\.*)',line,re.M|re.I)
if matchObj:
    print("matchObj.group(): ",matchObj.group())
    print("matchObj.group(1): ",matchObj.group(1))
    print("matchObj.group(2): ",matchObj.group(2))
else:
    print("string not found ")
string = matchObj.groups()
print("matchObj.groups(): ", string)
