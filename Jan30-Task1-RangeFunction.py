#Jan 30 Task1:

'''
range() - Built-in function.it returns a sequence of numbers
Syntax: range(start,stop,step)
start-optional; stop-required; step-optional
'''

#Using Range function  print multiples of 5 from 0 to 75
print("multiples of 5 from 0 to 75:")
for i in range(76):
    if i%5==0:
        print(i)
#Using Range function  print multiples of 8 from 0 to 72
print("multiples of 8 from 0 to 72:")
for i in range(73):
    if i%8==0:
        print(i)
#Using Range function  print multiples of 5 from 75 to 0
print("multiples of 5 from 75 to 0:")
for i in range(75,0,-1):
    if i%5==0:
        print(i)
#Using Range function  print multiples of 8 from 96 to 72
print("multiples of 8 from 96 to 72:")
for i in range(96,71,-1):
    if i%8==0:
        print(i)
        
