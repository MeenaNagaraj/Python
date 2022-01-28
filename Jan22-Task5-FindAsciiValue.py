s1=input("Enter String1:")
s2=input("Enter String2:")
mid_s1=s1[len(s1)//2]
mid_s2=s2[len(s2)//2]
print("Strings middle char is {} and String2 middle char is {}".format(mid_s1,mid_s2))

#ord() function used to find ASCII value
x=ord(mid_s1)
y=ord(mid_s2)
print("ASCII values for middle characters {},{} are {} and {}".format(mid_s1,mid_s2,x,y))

print("ASCII value of {} + ASCII value of {} = {}".format(mid_s1,mid_s2,x+y))
