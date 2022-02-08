#write a function to Find factors of a number
def find_factors(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i)


x=int(input("Enter number"))
find_factors(x)

'''
output
Enter number155
1
5
31
155
'''
