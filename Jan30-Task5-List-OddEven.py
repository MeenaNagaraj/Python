'''
Jan30 -Task 5:

Input:
Li1 = [3,4,5,2,7,8,9,10]

Output:
Li_odd = [3,5,7,9]
Li_even = [4,2,8,10]
'''

Li1 = [3,4,5,2,7,8,9,10]
odd=[]
even=[]
for i in Li1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Given List : ",Li1)
print("ODD : ",odd)
print("EVEN : ",even)

'''
output

Given List :  [3, 4, 5, 2, 7, 8, 9, 10]
ODD :  [3, 5, 7, 9]
EVEN :  [4, 2, 8, 10]

''''
