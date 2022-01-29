#mark calculation

#collect physics / checmistry / mathematics mark from user
#all the marks should be between 0 -200 ==> 
#calculate aggregate = phy/4  + chem/4  + maths / 2

#pass mark: 70

num1=int(input("Enter Physics Mark:"))
num2=int(input("Enter Chemistry Mark:"))
num3=int(input("Enter Mathematics Mark:"))

#Check valid or invalid marks
if (num1>=0 and num1<=200) and (num2>=0 and num2<=200) and (num3>=0 and num3<=200):
    print("Valid")

#Check Pass or Fail
    if num1>=70 and num2>=70 and num3>=70:
        print("Pass")
        
#calculate aggregate
        agg=int((num1/4)+(num2/4)+(num3/2))
        print("Your Aggregate Value is ",agg)
#Check Class
        if agg>=190:
            print("First Class")
        elif agg>=150:
            print("Second Class")
        elif agg>=70:
            print("Third Class")
    else:
        print("Fail... Try again")
else:    
    print("Invalid Mark.Enter a valid mark")
