#Fizz buzz
#Get one number from user
#5
#Multiple of 3 ==> Fizz
#Multiple of 5 ===> buzz
#Multiple of 3 and 5 ===> Fizzbuzz
#None ==> Invalid number

n=int(input("Enter Number:"))
if  n%3==0 and n%5==0:
    print("FizzBuzz \nMultiply of 3 and 5")
elif n%5==0:
        print("Buzz \nMultiply of 5")
elif n%3==0:
        print("Fizz \nMultiply of 3")
else:
    print("Invalid Number")
