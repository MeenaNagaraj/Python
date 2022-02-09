#1.abs() 
x,y=5,3+4j
print(abs(x),abs(y))   #o/p: 5 5.0

#2.all() any()
li=[True,True]
tu=(0,True)  #0 means false and 1 True
se={1,0,1}
mydict={0:"red", 1:45}  
print(all(li),all(tu),any(se))  #o/p: True False True 
x,y,z=5,50,33
if all((x>=0,x<25,y!=75,y<=100)):  
    print(x*y)                #o/p: 250
if any((x<=0, y==50, z>=50)):
    print(x+y+z)            #o/p:88

#3.bin()- result starts with 0b , ascii(), bool -result True or False
x=78
print(bin(x),ascii(x),bool(x)) #o/p: 0b1001110 78 True

#4.chr()-returns character for specified unicode code.
#ord()- return integer fot specied character
x=chr(97)
print(x) #o/p: a
y=ord("A")
print(y)  #o/p: 65

#5.complex()- returns complex number for specied real number and imaginary number
x=complex(3,5) #3-real number: 5-imaginary number
print(x) #o/p: (3+5j)

#6.divmod(arg1,arg2)-returns a tuple containing quotient & remainder
#arg1-dividend: arg-2divisor
x=divmod(5,2)
print(x)   #o/p: (2, 1)

#7.enumerate()- conver a collection(tuple) into enumerate objects
#function adds a counter as the key of the enumerate object
x=('red','green','orange')
y=enumerate(x)
print(list(y))  #o/p:[(0, 'red'), (1, 'green'), (2, 'orange')] 

#8.eval(expression)- evaluate expression, whether it's a legal python stmt
#it accepts single expression
x='print(75)'
eval(x)     #o/p: 75

#9.exec()- execute a block of code.it accepts large blocks of code
x='name="Kumar"\nprint(name)'
exec(x)   #o/p: Kumar

#10.filter(function,iterable)-returns an iterator were the items are filtered through a function
#to test if the item is accepted or not
num=[5,-7,10,-13,15,-19,20]
def myFunc(x):
    if x<0:
        return True
    else:
        return False
neg=filter(myFunc,num)
for x in neg:
    print(x,end=",") #o/p: -7,-13,-19,

#11.format(value,format)-formats a specified value into a specified format.
#format-legal values '<','>','^'-align left,right,center....
x=format(255,'x') #Hexadecimal format
y=format(251255, ',') #thousand separator
z=format(55, 'b')  #binary format
print(x) # o/p:ff
print(y) #o/p: 251,255
print(z) #o/p:110111

#12.help()-Executes the built-in help system
help('string') #Help on module string:

#13.id()-returns a unique id for the specified object.
#the object's memory address
x=5
y=id(x)
print(y) #o/p: 3019030397296

#14.isinstance(object,type)
x=isinstance(5,int)
y = isinstance(5, (str, float, str, list, dict, tuple))
print(y)    #o/p:False
print(x)   #o/p: True

#15.map(function,iterables)-executes a specified function for each item in an iterable.
def myfunc(a,b):
    return a+b
x=map(myfunc,('A','B','C','D'),('a','b','c','d'))
print(list(x))  #o/p: ['Aa', 'Bb', 'Cc', 'Dd']

#16.min(),max(),len()
a=(1,9,3,4,8,9)
print(min(a)) #o/p:1
print(max(a)) #o/p:9
print(len(a)) #o/p:6

#17.pow(x,y)-returns the value of x to the power of y.
x=pow(4,3)
print(x) #o/p:64

#18.range()-returns a sequence of numbers. starts from 0. default incremental value 1.
#range(start,stop,step)
for i in range(3,6):
    print(i, end=" ")    #o/p:3 4 5

#19.sorted(),reversed()
x=['f','d','a','e','c','b']
y=sorted(x)
print(y)  #o/p:['a', 'b', 'c', 'd', 'e', 'f']
ry=reversed(y)
for i in ry:
    print(i, end=" ")   #o/p: f e d c b a

#20.zip()
x = ("A", "B", "C")
y = ("Apple", "Banana", "Cherry")
a = zip(x, y)
    #use the tuple() function to display a readable version of the result:
print(tuple(a))

#o/p: (('A', 'Apple'), ('B', 'Banana'), ('C', 'Cherry'))



