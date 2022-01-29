#Create two tuples (1,4,5,6,7,8) (5,6,7,8,9)
#Find the common elements between two tuples
#Concatenate both tuples and remove duplicates from tuple
#Find the index value of 9 (after concatenation)
#multiply above elements 3 times


#Create two tuples (1,4,5,6,7,8) (5,6,7,8,9)
t1=(1,4,5,6,7,8)
t2=(5,6,7,8,9)
print("Tuple1:",t1,type(t1))
print("Tuple2:",t2,type(t2))

#Find the common elements between two tuples
#Concatenate both tuples and remove duplicates from tuple

#Tuple is 'unchangeable'
#use set()-is the collection of iterable and mutable data types with no duplicate elements
st1=set(t1)
st2=set(t2)
#print(st1,type(st1))
#print(st2,type(st2))

#Find Common element
#intersection() - return set that contains items that exist in both sets

com_item=st1.intersection(st2)
t3=tuple(com_item)
print("Common Elements between Tuple1 and Tuple2:",t3,type(t3))


#Find the index value of 9 (after concatenation)
tAdd=t1+t2
t4=tuple(set(tAdd))
print("Tuple Add:",t4)
print("Index Value of 9 is ",t4.index(9))

#multiply above elements 3 times
print("Multiple Tuple Elements 3 times:",t4*3)


