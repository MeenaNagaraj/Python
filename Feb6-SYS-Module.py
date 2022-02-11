#Sys Module -System Specific Function

'''
-provides functions and variables which are used to manipulate
different parts of the Python Runtime Environment
-allows operating on interpreters'''

import sys

#1.sys.version() - return version of Python Interpreter with aditional info.
print(sys.version)      #o/p:3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)]


#2.sys.path()- show Pythonpath set in the current system.
print(sys.path)     #o/p:['F:/Python Program/Task', 'C:\\Users\\ADMIN\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\idlelib',...]

#3.sys.builtin_module_names() - return names of all modules that are compiled into this Python interpreter
#tuple format
print(sys.builtin_module_names)     #o/p:('_abc', '_ast', '_bisect', '_blake2', '_codecs', '_codecs_cn', '_codecs_hk', '_codecs_iso2022', '_codecs_jp',...)

#4.sys.platform() -helps us to know about the platform
print("\nplatform: ",sys.platform)      #o/p: platform: win32

#5.sys.stdin.readline()- another way of getting input
print("Enter your data: ")
data=sys.stdin.readline()
print("Your data is "+data)     #o/p:Your data is Python programming

#6.sys.exit()
print("Hello world")
sys.exit()
print("welcome")        #o/p:Hello world


