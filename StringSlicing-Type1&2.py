# String Slicing - Type 1 and Type 2
# String1 sample
print("String Slicing - Type 1 and Type 2")
val="Information*Technology"
#Type1 - Slice[start:end] - Using strat and end
print("\nString 1 =",val)
print("\nType1")
print("\nval[3:10]=",val[3:10])
print("val[2:5]=",val[2:5])
print("val[0:10]=",val[0:10])
print("val[5:-5]=",val[5:-5])
print("val[2:8]=",val[2:8])
print("val[:8]=",val[:8])
print("val[5:]=",val[5:])
print("val[8:12]=",val[8:12])
print("val[:]=",val[:])
print("val[12:5]=",val[12:5])
#Type2 - Slice[start:eng:step] - Using start,end and step(stride)
print("\nType2\n")
print("val[3:10:1]=",val[3:10:1])
print("val[3:10:2]=",val[3:10:2])
print("val[3:10:3]=",val[3:10:3])
print("val[5:-5:1]=",val[5:-5:1])
print("val[5:-5:2]=",val[5:-5:2])
print("val[5:-5:5]=",val[5:-5:5])
print("val[:8:4]=",val[:8:4])
print("val[5::3]=",val[5::3])
print("val[::2]=",val[::2])
print("val[12:5:3]=",val[12:5:3])

#Strin2 sample
val="Python_Interpreter"

#Type1
print("\nString 2 =",val)
print("\nType1")
print("\nval[3:10]=",val[3:10])
print("val[2:5]=",val[2:5])
print("val[0:10]=",val[0:10])
print("val[5:-5]=",val[5:-5])
print("val[2:8]=",val[2:8])
print("val[:8]=",val[:8])
print("val[5:]=",val[5:])
print("val[8:12]=",val[8:12])
print("val[:]=",val[:])
print("val[12:5]=",val[12:5])

#Type2
print("\nType2\n")
print("val[3:10:1]=",val[3:10:1])
print("val[3:10:2]=",val[3:10:2])
print("val[3:10:3]=",val[3:10:3])
print("val[5:-5:1]=",val[5:-5:1])
print("val[5:-5:2]=",val[5:-5:2])
print("val[5:-5:5]=",val[5:-5:5])
print("val[:8:4]=",val[:8:4])
print("val[5::3]=",val[5::3])
print("val[::2]=",val[::2])
print("val[12:5:3]=",val[12:5:3])

