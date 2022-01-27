x1=input("Enter Name1 and Mark%(Float):")
x2=input("Enter Name2 and Mark%(Float):")
x3=input("Enter Name3 and Mark%(Float):")

#Spilt&Indexing
d1=x1.split()
d2=x2.split()
d3=x3.split()

#str to float convertion 
m1=float(d1[1])
m2=float(d2[1])
m3=float(d3[1])
#print(m1,type(m1))
add=m1+m2+m3
#print(type(add))
print("The Sum of Mark1- {1}, Mark2- {2} and Mark3- {3} is {0:.5f}".format(add,m1,m2,m3))
