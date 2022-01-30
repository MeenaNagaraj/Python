'''
Jan30- Task4:

Get two integers from user
print multiples of 8 between them
'''
x=int(input("Enter Value1 "))
y=int(input("Enter Value2 "))
li=[]
#if - not negative value and not zero
if x>0 and y>0:
    for i in range(x,y+1):
      if i%8==0:
          li.append(i)
    print("Multiples of 8 between {} and {} is \n{}".format(x,y,li))
else:
    print("Enter a valid number")

'''
output

Enter Value1 1
Enter Value2 80
Multiples of 8 between 1 and 80 is 
[8, 16, 24, 32, 40, 48, 56, 64, 72, 80]
'''
