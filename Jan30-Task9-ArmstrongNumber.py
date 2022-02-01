'''
Jan30-Task9
Armstrong number
*is a number that is equal to the sum of cubes of its digits.
*Eg: 0, 1, 153, 370, 371 and 407
*Eg: 153 = (1*1*1)+(5*5*5)+(3*3*3)
'''
n=int(input("Enter Number:"))

num=n
arm=0

#find remainder to get last digit,by using % operator
#find quotient to get next in loop , by using // floor division
#loop continue till num>0 condition is true

while num>0:
    rem=num%10
    num=num//10
    arm=arm+rem**3

if arm==n:
    print("YES! Given number {} is an armstrong number.".format(n))
else:
    print("NO! Given number {} is not an armstrong number.".format(n))


''''
output
Enter Number:153
YES! Given number 153 is an armstrong number.

output
Enter Number:157
NO! Given number 157 is not an armstrong number.
'''
