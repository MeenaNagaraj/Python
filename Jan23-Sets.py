#Create two empty sets
#update set1 with 7,8,9,1,2,3,4,5,0
#update set2 with 4,5,6,0
#check whether set2 is subset of set1 or no ?
#check whether both have common elements are no ?
#remove 8 from set 1 and set 2 ==> find the inferences
#discard 0 from set1 and set2 
#find collection of both sets ===> set1 and set2

#Create two empty sets
s1=set()
s2=set()

#update set1 with 7,8,9,1,2,3,4,5,0
#update set2 with 4,5,6,0
d1={7,8,9,1,2,3,4,5,0}
d2={4,5,6,0}
s1.update(d1)
s2.update(d2)
print("Set1: ",s1)
print("Set2: ",s2)

#check whether set2 is subset of set1 or no ?
#issubset() method
print("Set2 is subset of Set1 ?:",s2.issubset(s1))

#check whether both have common elements are no ?
if (s1&s2):
    print("Both have common value")
else:
    print("Both Do not have common value")

#remove 8 from set 1  ==> find the inferences
s1.remove(8)
print("Set1 after 8 from",s1)
x=s1.intersection(s2)
print("Intersection of Set1 and Set2 is",x)

#discard 0 from set1 and set2
s1.discard(0)
s2.discard(0)
print("Discard 0 from set1 - ",s1)
print("Discard 0 from set2 -",s2)

#find collection of both sets ===> set1 and set2
#Find union of set1 and set2
z=s1.union(s2)
print("Union of Set1 and Set2  ",z)


