#Get one mark from student
#mark 0 to 100 otherwise invalid mark
#50 + PASS otherwise FAIL
#90 to 100 ===> A 
#80 to 89 ===> B
#70 to 79 ===> C
#60 to 69 ===> D
#50 to 59 ===> E
#0 to 49 ===> FAIL

m=int(input("Enter Mark:"))
if m>=0 and m<=100:
    print("Valid Mark")
    if m>=50:
        print("PASS")
        if m>=90:
            print("Grade A")
        elif m>=80:
            print("Grade B")
        elif m>=70:
            print("Grade C")
        elif m>=60:
            print("Grade D")
        else:
            print("Grade E")
    else:
        print("Fail")
    
else:
    print("Invalid Mark.Please enter mark between 0 to 100")


