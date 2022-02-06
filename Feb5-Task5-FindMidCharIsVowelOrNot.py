#write a function to return whether middle character is vowel or not

def mid_char(s):
    y=s[len(s)//2]
    if (y=="a" or y=="e" or y=="i" or y=="o" or y=="u" or y=="A" or y=="E" or y=="I" or y=="O" or y=="U"):
        print("Yes")
    else:
        print("No")
    return 

s1=input("Enter String: ")
print(mid_char(s1))

'''
output

Enter String: red
Yes
None

Enter String: one
No
None

'''
