#Find factors of a number
n=int(input("Enter Number:"))
fact=[]
'''
#List
for i in range(1,n-1):
    if n%i==0:
        fact.append(i)
print("Factors of {} are:\n{}".format(n,fact))
'''
print("Factors of {} are:".format(n))
for i in range(1,n+1):
     if n%i==0:
        print(i)
'''
output
 =========
Enter Number:25
Factors of 25 are:
1
5
25

output
Enter Number:38
Factors of 38 are:
1
2
19
38

'''
