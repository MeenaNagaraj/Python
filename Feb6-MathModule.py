#Math Modules:
import math
#1.math.ceil() Method - Round a number upward to its nearest integer
print(math.ceil(1.4))   #o/p:2
print(math.ceil(-5.3))  #o/p:-5
print(math.ceil(10.0))  #o/p:10

#2.math.floor() Method - Round a number down to its nearest integer
print(math.floor(1.4))   #o/p:1
print(math.floor(-5.3))  #o/p:-6
print(math.floor(10.0))  #o/p:10

#3.math.comb() Method - total number of possibilities to choose k things from n items
#k>n return 0: -ve parameter - valueError: non-int paramter-TypeError
n,k=7,5
print(math.comb(3,2))   #o/p: 3
#print(math.comb(-3,-2)) #o/p: ValueError: n must be a non-negative integer

#4.math.degrees() Method - Convert angles from radians to degree
print (math.degrees(1))     #o/p:57.29577951308232
print (math.degrees(90))    #o/p:5156.620156177409
print(math.degrees(3.14))   #o/p:179.9087476710785 '(180 degree)'

#5.math.radians() Method - Convert degree values into radians
print(math.radians(180))    #o/p:3.141592653589793 '(3.14)'
print(math.radians(5156))   #o/p:89.98917623282763

#6.math.fabs() Method - unlike abs() it always return absolute value , as a float
print(math.fabs(-55.43))    #o/p: 55.43
print(math.fabs(-5))        #o/p: 5.0

#7.ath.factorial() Method - find the factorial of a number. accepts only +ve numbers
print(math.factorial(5))    #o/p: 120

#8.math.fmod(x,y) Method - return the remainder.(modulo)
#x,y==0 then ValueErroe: y==0 then ValueError: x or y != a number then TypeError
print(math.fmod(9,2))   #o/p:1.0
print(math.fmod(9,5))   #o/p:4.0
#print(math.fmod(5,0))   #o/p: ValueError: math domain error

#9.math.remainder() Method-Returns the closest value
#that can make numerator completely divisible by the denominator
print(math.remainder(9,2))  #o/p:1.0
print(math.remainder(9,5))  #o/p:-1.0


#10.math.fsum() Method- return sum of all items in any iterables(tuple, list,array)
print(math.fsum([1,2,3,4]))     #o/p: 10.0
print(math.fsum((10,20,30,40)))     #o/p: 100.0

#11.math.isclose() Method - Check whether two values are close to each other, or not:
print(math.isclose(1.233,1.32))     #o/p:False
print(math.isclose(1.0,1))          #o/p:True

#12.math.pow() Method - returns the value of x raised to power y.
print(math.pow(2,3))    #o/p:8.0

#13.math.prod() Method - return the product of the elements from the given iterable.
print(math.prod([1,2,3]))   #o/p:6

#14.math.sqrt() Method - returns the square root of a number
#number should be n>=0
print(math.sqrt(9))     #o/p:3

#15.math.pi Constant - print the value of PI
print(math.pi)  #o/p:3.141592653589793




