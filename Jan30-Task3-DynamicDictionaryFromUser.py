#Jan30-Task3:
#Get a dynamic dictionary from user
dic1={}
length=int(input("Enter length of the dictionary: "))
for i in range(0,length):
    key=input("Enter Key ")
    value=input("Enter Value ")
    dic1[key]=value
print("Your Dictionary is ",dic1,type(dic1))


'''
output
Enter length of the dictionary: 5
Enter Key 5
Enter Value Red
Enter Key 10
Enter Value Green
Enter Key 15
Enter Value Orange
Enter Key 20
Enter Value Pink
Enter Key 25
Enter Value Brown
Your Dictionary is  {'5': 'Red', '10': 'Green', '15': 'Orange', '20': 'Pink', '25': 'Brown'} <class 'dict'>
'''
