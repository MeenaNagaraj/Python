#write a function to  Find Fibnacci series
def find_fibo(nterms):
    n1,n2=0,1
    count=0
    if nterms<=0:
        print("Enter positive number")
    elif nterms==1:
        return 0
    else:
        while count<nterms:
            print(n1)
            n3=n1+n2
            n1=n2
            n2=n3
            count=count+1
    return


n=int(input("Enter - how many terms: "))
if n<=0:
    print("Enter positive number")
else:
    find_fibo(n)

'''
output
Enter - how many terms: 0
Enter positive number

output
Enter - how many terms: 9
0
1
1
2
3
5
8
13
21
'''
