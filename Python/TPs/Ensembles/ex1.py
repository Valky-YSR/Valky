ens = {"kalbon",12,False,2.718}
ens2 = {12,1337,2.718}
ens1 = ["ayywa"]
ens.add("mshish")

ens.update(ens1)
ens.remove(12)
ens.pop()
ens.clear()
ens.discard("prtscr")
print(ens)
print("Nombre d'element: ",len(ens))
print("somme : ",sum(ens2) )
print("max",max(ens2))
print("min : ",min(ens2))
# 
ens3 = {16,19,10}
ens4 = ens3.copy()
ens3.add(20)
print(ens3)
print(ens4)
ens5 = frozenset(ens3)
print(ens5)

enss = {"mshish","klb", 12, True, 1337}
ensss = {"kalbon","qalomba", 1337}
print(enss.difference(ensss))
print(enss.intersection(ensss))
print(enss.union(ensss))

print(enss.isdisjoint(ensss))