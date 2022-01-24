print("Area of the Cirle")

#Formula pi*r^2

pi=3.14
r=float(input("Enter The Radius Value:"))
area=int(pi*r*r) # we can use r**2 instead of r*r

print("\nThe area of the circle with radius ",r," is ",area)

print("\nRadius Value Type --> ",type(r))
print("Area Value Type -->",type(area))
