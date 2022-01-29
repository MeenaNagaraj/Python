#create empty list
list1=[]
list2=list()
print("Two Empty Lists:",list1,list2)

#Concatenate with [5,6,7,8]
list3=[5,6,7,8]
list4=list1+list3
print(list4)

#add 8,9,1,5,6,7,8,1 elements to that list
list5=[8,9,1,5,6,7,8,1]
#list4=list4+list5
list4.extend(list5)
print(list4)

#Find frequency of 8 (count)
c=list4.count(8)
print("Find frequency of 8 (count) is ",c)

#find the mean of the list, sum (List), min, Max
list4_sum=sum(list4)
list4_len=len(list4)
list4_mean=int(list4_sum/list4_len)
print(list4_sum)
print(list4_len)
print(list4_mean)
print(min(list4))
print(max(list4))

#Find median of the list.
#the middle number in a sorted, ascending or descending, list of numbers
list4.sort()
print(list4)
list4_mid=int(list4_len//2)
print(list4[list4_mid])

#remove duplicates from list, using set()
list5=set(list4)
print(list5)

#set to tuple conversion
x=tuple(list5)
print(x,type(x))


