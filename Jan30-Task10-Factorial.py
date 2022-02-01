#Find factorial of a number
n=int(input("Enter Number:"))

#for loop
fact=1
for i in range(1,n+1):
    fact=fact*i
print("Factorial value of {} is {}".format(n,fact))

'''
#while loop
fact=n
while n>1:
    n=n-1
    fact=fact*n
print(fact)
'''

'''
output
Enter Number:7
Factorial value of 7 is 5040
'''
