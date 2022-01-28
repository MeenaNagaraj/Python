x="Python New"

#center() --> Returns a centered string
#a=x.center(75) 
print(x.center(55)) #str.center(length) --->default char is space
print(x.center(55,"x")) #str.center(length,char)

#rjust()
print("\n",x.rjust(25,"*"))

#ljust()
print(x.ljust(25,"*"))

#isalpha() , isnumeric() and islower() methods
s="python3"
print("\n\nYour String is ",s)
print("String",s,"is isalpha() -",s.isalpha()) #Returns True if all chars in string are alphabet
print("String",s,"is isnumeric() -",s.isnumeric())
print("String",s,"is islower() -",s.islower())




