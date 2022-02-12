import random

li=["rock","paper","scissor"]
u_count=0
s_count=0
t_count=0
n=int(input("How many games do u want to play? :"))
if n>0:
    for i in range(1,n+1):
        print("\nGame: ",i)
        user=input("\nGive your input['rock','paper','scissor'] :").lower()
        if user=="rock" or user=="paper" or user=="scissor":
            sys=random.choice(li)
            print("\nyour input: {}\nSystem Input: {}".format(user,sys))
            if user==sys:
                print("Tie")
                t_count=t_count+1
            elif user!=sys:
                if ((user=="rock" and sys=="scissor")or(user=="scissor" and sys=="paper")or(user=="paper" and sys=="rock")):
                    u_count=u_count+1
                    print("User Win \nUser Points: {}".format(u_count))
                else:
                    s_count=s_count+1
                    print("System Win\nSystem Points: {}".format(s_count))
            else:
                print("Invalid")
        else:
             print("Invalid Option. Enter valid option")
    print("\n\nTOTAL POINTS SCORED:")
    print("Total Number of Games: {}\nUser Points: {}\nSystem Points: {}\nTie Count: {}".format(n,u_count,s_count,t_count))
    print("\n\nRESULT:")
    if u_count==s_count:
        print("It is Tie.")
    elif u_count>s_count:
        print("USER wins the game!!! Congrats!!!")
    else:
        print("SYSTEM wins the game!!!")
else:
    print("Invalid Number. Enter a valid number")
