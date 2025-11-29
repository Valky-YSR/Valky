total = 20 
bus = []

def res():
    nom=input("Entrer votre nom :")
    dest=input("Entrer votre destination :")
    prix=int(input("Entrez le prix de billet :"))
    ajr = [nom,dest,prix]
    bus.appqend(ajr)

    print("La reservation de",nom,"a été ajouté aves succes.")
    
def aff():
   if bus==[]:
      print("Ce bus est vide.")
   else :
      print("Liste des réservations disponibles")
      for i, valeur in enumerate (bus, start=1): 
          print(i,".", valeur[0],"-",valeur[1],valeur[2])
#    with open("res.txt", "a", encoding="UTF-8") as f:
    #   print(f.readlist(ajr)) # type: ignore
def ann():
   aff()
   if bus==[]:
    choix = int(input("entrer le nemuro du reservation a annuler :"))
    if 1 <= choix <= len(bus):
       res_ann=bus.pop(choix -1)
       print("La reservation", res_ann[0],"é ete supprime.")
   else :
    print("Numero invalide.")
   
   while True :
 
print("====Gestion de réservation====")
print("1. Ajouter une réservation")
print("2. Afficher la liste des réservations")
print("3. Annuler une réservation")
print("4. Afficher les places restantes")
print("5. Quitter.")

choix=input("Choisir un choix :")

if choix == "1":
    res()
elif choix == "2":
    aff()
elif choix == "3":
    ann()
elif choix == "4":
    aff()
elif choix == "5":
    print("Quittant le programme.")
    break        
else :
    print("choix invalide, ressayer.")
