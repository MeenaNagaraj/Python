# write a function to check whether number is armstrong number or no
def find_arms(n):
    arm=0
    len_n=len(str(n))
    while n>0:
        rem=n%10
        n=n//10
        arm=arm+(rem**len_n)
    return arm

num=int(input("Enter Number: "))
num1=num

if find_arms(num1)==num:
    print("Yes. Given number {} is an Armstrong Number".format(num))
else:
    print("No. Given number {} is not an Armstrong Number".format(num))

'''
output
Enter Number: 9474
Yes. Given number 9474 is an Armstrong Number

output
Enter Number: 153
Yes. Given number 153 is an Armstrong Number
'''
