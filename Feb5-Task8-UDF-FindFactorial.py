#write a function to Find factorial of a number
def find_factorial(f):
    fact=1
    for i in range(1,f+1):
        fact=fact*i
    return fact

n=int(input("Enter Number: "))
print("Factorial of {} is {}.".format(n,find_factorial(n)))

'''
output
Enter Number: 5
Factorial of 5 is 120.

'''
