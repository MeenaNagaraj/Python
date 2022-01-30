'''
Task6:

Input: [-1, -7,8,10,20,21,17,28,-3,0,0,]
    
Output:
neg_LI = [-1,-7,-3]
pos_LI = []
Zeros = []

Numeber of postivie ele: 7
Number nega: 3
Number of zeros: 2
'''
li= [-1, -7,8,10,20,21,17,28,-3,0,0]
n_li=[]
p_li=[]
z_li=[]

for i in li:
    if i==0:
       z_li.append(i)
    elif i<0:
        n_li.append(i)
    else:
        p_li.append(i)
print("Given List: ",li)
#lists
print("P_List: ",p_li)
print("L_List: ",n_li)
print("Z_List: ",z_li)
#counts
print("Nember of positive elements: ",len(p_li))
print("Nember of negative elements: ",len(n_li))
print("Nember of zero elements: ",len(z_li))

'''
output

Given List:  [-1, -7, 8, 10, 20, 21, 17, 28, -3, 0, 0]
P_List:  [8, 10, 20, 21, 17, 28]
L_List:  [-1, -7, -3]
Z_List:  [0, 0]
Nember of positive elements:  6
Nember of negative elements:  3
Nember of zero elements:  2
'''
