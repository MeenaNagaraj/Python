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

'''        
Output
multiples of 5 from 0 to 75:
0
5
10
15
20
25
30
35
40
45
50
55
60
65
70
75
multiples of 8 from 0 to 72:
0
8
16
24
32
40
48
56
64
72
multiples of 5 from 75 to 0:
75
70
65
60
55
50
45
40
35
30
25
20
15
10
5
multiples of 8 from 96 to 72:
96
88
80
72
'''
