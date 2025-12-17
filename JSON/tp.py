import json
# 
# with open("tp.json", "r", encoding="utf-8")as f:
    # data=json.load(f)
# print(data["modules"])
# 
# string_json= '{"nom":"kalbon","Prenom": "mshish","age":90}'
# data1= json.loads(string_json)
# print(data1["nom"])

etudiant={
    "nom": "klb",
    "age": 20,
    "niveau": "3yén"
    }

with open("tp.json", "w", encoding="utf-8") as f:
    data2=json.dump(etudiant,f,indent=2, ensure_ascii=False)
print(etudiant)

for cle,valeur in data.items():
    print(cle," : ",valeur)

print('--------')
for module in data["modules"]:
   print(cle," : ",valeur)
print(module)

print('--------')

for cle, valuer in data["adresse"]:
    print(cle," : ",valeur)
print('--------')
