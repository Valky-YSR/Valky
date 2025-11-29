string = "Welcome to WeBox"
index = -1
char = "o"
print(string)
choice=input("Entrez l'indice d'un caractere")
for n in range(len(string)):
    if string[i] == char :
        index = i 
        break
    if index != -1 :
    print("1ere occurence de",string,"a l'index",index)
else :
    print("caractere",char,"non trouve")
