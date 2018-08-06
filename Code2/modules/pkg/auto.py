import os,shutil,sys
curdir=os.getcwd()
os.mkdir('c://mypkg')
os.chdir('c://mypkg')
os.mkdir('mod')
os.chdir('mod')
f = open('pat.py','w')
s = """
def pat(n):
    for i in range(n):
        for j in range(i):
            print('*',end='')
        print()
        """
f.write(s)
f.close()
f = open('calc.py','w')
s = """
def add(a,b):
    print("REsult = ",a+b)
    """
f = open("__init__.py",'w')
s = """
from . import calc
from . import pat
"""
f.write(s)
f.close()
os.chdir('../')
f = open('test.py','w')
s = """
import mod
mod.pat.pat(10)
mod.calc.add(45,45)
"""
f.write(s)
f.close()
os.system('python c://mypkg//test.py')
