#Write a function to return middle char of the string

def mid_char(s):
    y=len(s)//2
    return s[y]

s1=input("Enter String: ")
print(mid_char(s1))

'''
output

Enter String: computer
u

Enter String: red
e

'''
