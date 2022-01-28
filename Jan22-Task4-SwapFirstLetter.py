s1=input("Enter String 1:")
s2=input("Enter String 2:")
print("Your Strings are :{}{}".format(s1,s2))

#Find First Letter
sw_s1=s1[0]
sw_s2=s2[0]
print("First Letters of your strings are: ",sw_s1,sw_s2)

#Swaping first letter
replace_s1=s1.replace(s1[0],s2[0])
replace_s2=s2.replace(s2[0],s1[0])
print("After swaping first letters, Your strings are:{}{}".format(replace_s1,replace_s2))

#Find Length of string
length_s1=len(s1)
length_s2=len(s2)
print("String1 length is {} and String2 length is {}".format(length_s1,length_s2))

#Find middle letter of string
midLet_s1=length_s1//2
midLet_s2=length_s2//2
print("String1 middle letter is {} and String2 middle letter is {}".format(s1[midLet_s1],s2[midLet_s2]))


print("\nYour OutPut is",replace_s1+replace_s2+str(length_s1)+str(length_s2)+s1[midLet_s1]+s2[midLet_s2])
