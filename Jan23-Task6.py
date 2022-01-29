
a = {1: [1,2,3,"python"],
     2:{10:"hello",20:"welcome",40: "science"},
     99: {3,4,5,6},
     40:{1:"zoology", 2:"Botany"}}

#py
print(a.get(1)[3][:2])
#ello
print(a.get(2)[10][1:])
#en
print(a.get(2)[40][3:5])
#zoo
print(a.get(40)[1][:3])
#Bot
print(a.get(40)[2][:3])
