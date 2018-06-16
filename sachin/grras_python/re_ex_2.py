import re
phone = "0141-227-166 #my phone no. "
num = re.sub(r'#.*$',"",phone)
print("sub no. = ",num)
num = re.sub(r'\D',"",phone)
print("sub \D = ", num)
