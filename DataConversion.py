print("Data Conversion")

print("\n1. Data Conversion from Integer to Float, Boolean and String.")

value1=25
print("Integer Number : ",value1,type(value1))
value_new=float(value1)
print("\nFloat Value : ",value_new,type(value_new))
value_new=bool(value1)
print("Boolean Value : ",value_new,type(value_new))
value_new=str(value1)
print("String Value  : ",value_new,type(value_new))

print("\n2. Data Conversion from Float to Integer, Boolean and String.")
value1=75.65895
print("Float Value : ",value1,type(value1))
value_new=int(value1)
print("\nInteger Value : ",value_new,type(value_new))
value_new=bool(value1)
print("Boolean Value : ",value_new,type(value_new))
value_new=str(value1)
print("String Value : ",value_new,type(value_new))

print("\n3. Data Conersion from String to Intger, Float and Boolean.")
value1= "50"
print("String Value  :",value1,type(value1))
value_new=int(value1)
print("\nInteger Value  :",value_new,type(value_new))
value_new=float(value1)
print("Float Value  : ",value_new,type(value_new))
value_new=bool(value1)
print("Boolean Value : ",value_new,type(value_new))

print("\n4. Data Conversion from Boolean to Integer, Float and String.")
value1=True
print("Boolean Value : ",value1,type(value1))
value_new=int(value1)
print("\nInteger Value : ",value_new,type(value_new))
value_new=float(value1)
print("Float Value : ",value_new,type(value_new))
value_new=str(value1)
print("String Value : ",value_new,type(value_new))
