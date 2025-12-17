import json
produits=[id_produit,nom_produit]
def ajouter():
    id_produit=input("Entrez l'ID de produit: ")
    if id_produit in produits:
        print("Le produit deja existe")
        return
    nom_produit=input("Entrez le nom de produit: ")
    produits[id_produit]={
        "ID": id_produit,
        "Nom": nom_produit
    }
def rechercher():
    print("""Chercher par : 
    | 1 | L'ID du produit
    | 2 | Le nom du produit
    """)
    choix1=input("Veuillez chercher par L'ID ou le nom ?")
if choix  == "1":
    id_produit=int(input("Entrez l'ID de produit"))
    if id_produit in produits:
        produit=produits[id_produit]
        print(f"""
        ID : {id_produit}
        Nom : {nom_produit}
        """)
    else:
        print("Ce produit n'existe pas.")
elif choix1 == "2":
    nom_produit=(input("Entrez le nom du produit" ))
    if nom_produit in produits:
        produit= produits[nom_produit]
        print(f"""
        ID: {id_produit}
        Nom: {nom_produit}
        """)
    else:
        print("Ce produit n'existe pas : ")
def modifier():
    id_produit=input("Entrez l'id du produit a modiifier")
    
def supprimer():
    id_prduit=int(input("Entrez l'ID du produit a supprimer"))
    if id_produit in prouduits:
        del produits[id_produit]
        print("Le produit a ete supprime !")
    else:
        print("Le produit n'existe pas.")
while True:
    print("""
    | 1 |       Ajouter un nouveau produit       |
    | 2 |          Rechercher un porduit         |
    | 3 | Modifier les informations d'un produit |
    | 4 |         Supprimer un produit           |
    | 5 |               Quitter                  |
    """)
choix=int(input("Veuillez saisir votre choix : "))
if choix == "1":
    pass
elif choix == "2":
    pass
elif choix == "3":
    pass
elif choix == "4":
    pass
elif choix == "5":
    print("Au revoir !")
    break
else:
    Print("Choix invalide, veuillez un saisir un nombre entre 1 et 5.")