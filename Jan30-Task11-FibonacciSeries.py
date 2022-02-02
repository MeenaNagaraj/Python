#Find Fibnacci series
n=int(input("Enter how many terms: "))

#initializing first two numbers with 0 and 1
x,y=0,1
if n<=0:
    print("Enter positive number")
elif n==1:
    print("Fibonacci series upto {} term : {}".format(y,0))
else:
    print("Fibonacci series upto {} terms are\n{}\n{} ".format(n,x,y))
    for i in range(2,n):
        z=x+y
        x=y
        y=z
        print(y)

'''
output

Enter how many terms: 0
Enter positive number

output

Enter how many terms: 5
Fibonacci series upto 5 terms are
0
1 
1
2
3

output
Enter how many terms: 1
Fibonacci series upto 1 term : 0

'''
