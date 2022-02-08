#write a function to check whether given number is prime or no

def find_prime(x):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True

def valid_check(y):
    if y>0:
        return True
    
n=int(input("Enter Number: "))
v=valid_check(n)
if v==True:
    if n>1:
        ans=find_prime(n)
        if ans==True:
            print("Yes. Given number {} is a Prime Number.".format(n))
        else:
            print("No. Given number {} is not a Prime Number.".format(n))
    else:
        print("invalid number")
else:
    print("please enter positive integer.")

'''
output
Enter Number: 149
Yes. Given number 149 is a Prime Number.

output
Enter Number: -5
please enter positive integer.

output
Enter Number: 7
Yes. Given number 7 is a Prime Number.

output
Enter Number: 149
Yes. Given number 149 is a Prime Number.


'''
