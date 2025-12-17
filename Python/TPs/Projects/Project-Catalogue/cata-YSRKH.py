produits = {}  # Dictionnaire vide pour stocker les produits

def ajouter_produit():
    id_produit = input("Entrez l'ID du produit : ")
    if id_produit in produits:
        print("Le produit existe deja")
        return
    nom_produit = input("Entrez le nom du produit : ")
    categorie = input("Entrez la categorie du produit : ")
    prix = float(input("Entrez le prix du produit : "))
    quantite_stock = int(input("Entrez la quantite en stock : "))
    statut = input("Entrez le statut du produit (Disponible, Rupture, Promotion): ")
    
    produits[id_produit] = {
        "nom": nom_produit,
        "categorie": categorie,
        "prix": prix,
        "quantite_stock": quantite_stock,
        "statut": statut
    }
    print("Le produit a ete ajoute!")

def recherche_produit():
    id_produit = input("Entrez l'ID du produit a chercher : ")
    if id_produit in produits:
        produit = produits[id_produit]
        print(f"""\n
ID: {id_produit}
Nom : {produit['nom']}
Categorie : {produit['categorie']}
Prix : {produit['prix']}dh
Quantite en stock : {produit['quantite_stock']}
Statut : {produit['statut']}
        """)
    else:
        print("Le produit n'existe pas.")

def mise_a_jour_prix():
    id_produit = input("Entrez l'id du produit dont le prix a modifier : ")
    if id_produit in produits:
        nouveau_prix = float(input("Entrez le nouveau prix : "))
        produits[id_produit]["prix"] = nouveau_prix
        print("Le prix a ete modifie!")
    else:
        print("Le produit n'existe pas.")

def mise_a_jour_quantite():
    id_produit = input("Entrez l'id du produit dont la quantite a changer : ")
    if id_produit in produits:
        nouvelle_quantite = int(input("Entrez la nouvelle quantite : "))
        produits[id_produit]["quantite_stock"] = nouvelle_quantite
        print("La quantite du produit a ete modifiee!")
    else:
        print("Le produit n'existe pas.")

def mise_a_jour_statut():
    id_produit = input("Entrez l'id du produit dont le statut a modifier : ")
    if id_produit in produits:
        nouveau_statut = input("Entrez le nouveau statut : ")
        produits[id_produit]["statut"] = nouveau_statut
        print("Le statut a ete modifie!")
    else:
        print("Le produit n'existe pas.")

def supprimer_produit():
    id_produit = input("Entrez l'id du produit a supprimer : ")
    if id_produit in produits:
        del produits[id_produit]
        print("Le produit a ete supprime!")
    else:
        print("Le produit n'existe pas.")

def afficher_catalogue():
    if not produits:
        print("Le catalogue est vide!")
        return
    
    print("\n=== CATALOGUE ===")
    for id_produit, produit in produits.items():
        print(f"ID: {id_produit} | Nom: {produit['nom']} | Prix: {produit['prix']}dh | Quantite: {produit['quantite_stock']} | Statut: {produit['statut']}")

while True:
    print("""
    Réalisé par : Yassir KHALFOUFI
    ========= Catalogue =========
    | 1 | Ajouter un produit    |
    | 2 | Rechercher un produit |
    | 3 | Modifier le prix      |
    | 4 | Modifier la quantite  |
    | 5 | Modifier le statut    |
    | 6 | Supprimer un produit  |
    | 7 | Afficher le catalogue |
    | 8 | Quitter               |
    ==============================
    """)
    choix = input("Entrez votre choix : ")
    if choix == "1":
        ajouter_produit()
    elif choix == "2":
        recherche_produit()
    elif choix == "3":
        mise_a_jour_prix()
    elif choix == "4":
        mise_a_jour_quantite()
    elif choix == "5":
        mise_a_jour_statut()
    elif choix == "6":
        supprimer_produit()
    elif choix == "7":
        afficher_catalogue()
    elif choix == "8":
        break
    else:
        print("Choix invalide")