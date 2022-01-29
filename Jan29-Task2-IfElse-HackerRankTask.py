n=int(input("Enter Number:"))
#print(n,type(n))
if n>=1 and n<=100:
#If n is odd, print Weird
    if n%2==0:
        print("Given Number is Even")
        if n>2 and n<5:
            print("Not Weird")
        if n>6 and n<20:
            print("Weird")
        if n>20:
            print("Not Weird")   
    else:
        print("Given Number is Odd")
        print("Weird")
else:
    print(" Your Number should be from 1 to 100.Please Enter a valid number")
