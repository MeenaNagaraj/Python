def str_palind(x):
   return x==x[::-1]
    
s1=input("Enter a string:")

result=str_palind(s1)

if result==True:
    print("Yes. Given string is palindrome.")
else:
    print("No. Given is not palindrome.")
