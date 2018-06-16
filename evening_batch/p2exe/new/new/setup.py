from cx_Freeze import setup, Executable
import os
os.environ['TCL_LIBRARY'] = r'C:\Anaconda\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Anaconda\tcl\tk8.6'


setup(name='calculator',
        version='0.1',
        description='calculator app for basic',
        executables=[Executable("tk_calc.py")])
