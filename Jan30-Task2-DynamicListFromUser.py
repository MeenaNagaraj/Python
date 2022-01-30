#Jan 30- Task 2
#Get a dynamic list from user

#create an empty list
list1=[]
#Collect list length from user using input() and convert into int 
length=int(input("Enter the length of the list: "))
#print(list1,type(list1),length,type(length))

for i in range(0,length):
    data=input("Enter list value{} :".format(i+1))
    list1.append(data)
print("Your List is ",list1)

'''
Output

Enter the length of the list: 5
Enter list value1 :Red
Enter list value2 :Green
Enter list value3 :Yellow
Enter list value4 :Orange
Enter list value5 :Pink
Your List is  ['Red', 'Green', 'Yellow', 'Orange', 'Pink']
'''
