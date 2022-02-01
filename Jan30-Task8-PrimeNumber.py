'''
Jan30-Task8

check whether number is prime or no.

Prime Number- A number that is divisible only by itself and 1.
* Prime numbers are natural numbers greater than 1.
* having only two factors, one and the number itself
* Prime numbers have exactly two factors therefore 0 and 1 are not prime numbers.
(Eg. 2,3,5,7,11,13,17,19)
'''
n=int(input("Enter Number: "))

#check 0 and 1 are not prime numbers. 
if n>1:
    
#for loop - check number from 2 to n
#if - check n is divisible by any other number between 2 to n
    for i in range(2,n):
        if n%i==0:
            print(n,"is not a prime number")
            break
    else:
        print(n,"is a prime number")
else:
    print(n,"is not a prime number")


'''
output

Enter Number: 55
55 is not a prime number

output
Enter Number: 97
97 is a prime number
'''
