#create a dictionary
#{1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}
#Extract "bobtn" from above dictionary
#Extract "arbeg" from above dictionary
#print all keys in dictionary and convert it into tuple
#Find the average of all numbers available under key "2"

#create a dictionary
#{1:["english","maths","science"], 2:[10,20,30],
# 3:["bio-botany","bio-zoology","Algebra"]}
d1={1:["english","maths","science"],
    2:[10,20,30],
    3:["bio-botany","bio-zoology","Algebra"]
    }
print(d1,type(d1))

#Extract "bobtn" from above dictionary

#print(d1[3])
#print(d1[3][0])
print(d1[3][0][::2])

#Extract "arbeg" from above dictionary
print(d1[3][2][:-6:-1])

#print all keys in dictionary and convert it into tuple
print(d1.keys())
t1=tuple(d1.keys())
print("Dictionary Keys to Tuple:",t1)

#Find the average of all numbers available under key "2"
l=len(d1)
s=sum(d1[2])
avg=s/l
print("Values under key 2 are:",d1[2])
print("Dictionary length is:",l)
print("Addition of values under key 2:",s)
print("Average of all values under key 2 is:",avg)

