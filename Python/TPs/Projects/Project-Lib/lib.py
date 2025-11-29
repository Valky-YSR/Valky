biblio = []

while True :

    print("========Menu========")
    print("1. ajouter un livre")
    print("2. Afficher les livres")
    print("3. Rechercher un livre")
    print("4. Supprimer un livre")
    print("5. Quitter")
    print("====================")

choice =input("choisissez un de ces opions :")
    if choice == 1 :
        ajt_livre()
    elif choice == 2 :
        aff_livre()
    elif choice == 3:
        search_livre()
    elif choice = 4 :
        sup_livre()
    elif choice == 5 :
        print("Quittant le programme.")
    else :
        print("Choix invalide, veuillez saisir un choix.")
    break
def ajt_livre():
    titre=str(input("Entrez le titre de livre:"))
    auteur=str(input("Entrez l'auteur du livre :"))
    annee=int(input("Entrez l'année :"))
    livre = [titre,auteur,annee]
    biblio.append(livre)
    print("Livre ",titre," a ete ajoute")
def aff_livre():
    if bilio = [] :
        print("Aucun livre dans la bibliotheque")
    else :
        prin("\n Liste des valeurs disponibles")
        for i, valeur in enumerate(biblio) :
            print(i+1,"."valeur[0],"-",valeur[1],valeur[2])
def search_livre() :
    mot_cle = input("Entrez le mot cle :").lower() 
    resultats = []
    for livre in biblio:
        if mot_cle in livre[0].lower() or mot_cle in livre[1].lower():
            resultats.appenc(livre)
    if resultats != [0] :
        print("\n Resultats de la recherche")
        for valeur in resultats:
            print(valeur[0],"-",valeur[1],valeur[2])
    else :
        print("\n Aucun livres disponibles.")
def sup_livre():
    aff_livre()
    if biblio != []:
        choice = int(input("entrez le num de livre a supprimer"))
        if 1 <= choice <= len(biblio):
            livre_supprime = livre.pop(choic-1)
            print("Le livre",livre_supprime[0],"a ete supprime")
    else :
        print("Numero invalide\n")
