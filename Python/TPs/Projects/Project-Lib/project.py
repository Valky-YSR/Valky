biblio = []

def ajt_livre():
    titre = input("Entrez le titre de livre:")
    auteur = input("Entrez l'auteur du livre :")
    try:
        annee = int(input("Entrez l'année :"))
    except ValueError:
        print("Année invalide. Valeur par défaut 0.")
        annee = 0
    livre = [titre, auteur, annee]
    biblio.append(livre)
    print("Livre", titre, "a ete ajoute")

def aff_livre():
    if not biblio:
        print("Aucun livre dans la bibliotheque")
    else:
        print("\n Liste des valeurs disponibles")
        for i, valeur in enumerate(biblio):
            print(i+1, ".", valeur[0], "-", valeur[1], valeur[2])

def search_livre():
    mot_cle = input("Entrez le mot cle :").lower()
    resultats = []
    for livre in biblio:
        if mot_cle in livre[0].lower() or mot_cle in livre[1].lower():
            resultats.append(livre)
    if resultats:
        print("\n Resultats de la recherche")
        for valeur in resultats:
            print(valeur[0], "-", valeur[1], valeur[2])
    else:
        print("\n Aucun livres disponibles.")

def sup_livre():
    aff_livre()
    if biblio:
        try:
            choice = int(input("entrez le num de livre a supprimer: "))
        except ValueError:
            print("Entrée invalide.")
            return
        if 1 <= choice <= len(biblio):
            livre_supprime = biblio.pop(choice-1)
            print("Le livre", livre_supprime[0], "a ete supprime")
        else:
            print("Numero invalide\n")
    else:
        print("Aucun livre à supprimer\n")

while True:
    print("========Menu========")
    print("1. ajouter un livre")
    print("2. Afficher les livres")
    print("3. Rechercher un livre")
    print("4. Supprimer un livre")
    print("5. Quitter")
    print("====================")
    print("\n")
    choice = input("Choisissez un option")
    if choice == "1":
        ajt_livre()
    elif choice == "2":
        aff_livre()
    elif choice == "3":
        search_livre()
    elif choice == "4":
        sup_livre()
    elif choice == "5":
        print("Quittant le programme.")
        break
    else:
        print("Choix invalide, veuillez saisir un choix.")