# tuple1=("dev",False,2,3.14,"y")
# print(tuple1)
# tuple2= tuple(("dev",False,2,3.14,"y"))
# print(tuple2)
# tuple3 = tuple(range(1,11))
# print(tuple3)

# pos = int(input("Saisir un nombre positif : "))
# print(tuple(range(1, pos + 1)))
# print(tuple(range(2, pos + 1, 2)))
# print(tuple(range(1, pos + 1, 2)))
# tab = (2,3,1,6,23,62,12,10)
# tab2 = (2,9,6,10,19,12,11,15)
# print(tab[0:3])
# tab3 = tab + tab2 
# print("tab + tab2 = ",tab3)
# print("Répétition :",tab * 2)


# t1 = ("Dev","104","Python")
# print("class :".capitalize(),t1[0])
# print("group :".capitalize(),t1[1])
# print("matiere :".capitalize(),t1[2])

#tp

# T1 = [3,1,0,2,4,5,7,6,9,8,10,11,19,12,18,17,16,15,14,13]
# T2 = tuple(range(2,16,5))
# T1 =(tuple(range(1,10,4)))
# print(tuple(range(2,16,5)))  
# T3 = T1 + T2
# print(T3)
# T4 = T1 * 2
# print(T4)
# print(T4 == T3)
# T5 = tuple(range(0,5,3)) + T2 * T3
# print(T5)


T1 = (1,2,3,4,5,6,7,8,9,10,5,)
T2 = ("kalbon")
print(len(T1))
print(max(T1))
print(min(T1))
print(T1.count(5))
print(tuple(sorted(T1)))
print(tuple(reversed(T1)))
print(T2.index("n"))

