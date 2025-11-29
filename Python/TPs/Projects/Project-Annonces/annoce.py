# TP7
# pour ajt des anncs 
def ajouter_annonces(annonces, id_annonce, titre, entreprise, ville, salaire):
    new_annonce = (id_annonce, titre, entreprise, ville, salaire)
    annonces = annonces + (new_annonce,)
    return annonces

def afficher_annonces(annonces):
    if len(annonces) == 0:
        print("Aucune annonce disponible")
        return
    for annonce in annonces:
        id_ann, titre, entreprise, ville, salaire = annonce
        print(f"ID: {id_ann} | {titre} | {entreprise} | {ville} | {salaire} DH")

def rechercher_annonces(annonces):
    print("\nRechercher par :")
    print("1. Titre")
    print("2. Ville")
    print("3. Entreprise")
    choix = input("Votre choix : ")
    
    if choix == "1":
        titre = input("Saisir le titre : ")
        for annonce in annonces:
            if annonce[1].lower() == titre.lower():
                print(f"Trouvé : {annonce}")
                return annonce
    elif choix == "2":
        ville = input("Saisir la ville : ")
        for annonce in annonces:
            if annonce[3].lower() == ville.lower():
                print(f"Trouvé : {annonce}")
                return annonce
    elif choix == "3":
        entreprise = input("Saisir l'entreprise : ")
        for annonce in annonces:
            if annonce[2].lower() == entreprise.lower():
                print(f"Trouvé : {annonce}")
                return annonce
    
    print("Aucune annonce trouvée")
    return None

def meilleur_offre(annonces):
    if len(annonces) == 0:
        print("Aucune annonce disponible")
        return None
    
    meilleure = annonces[0]
    for annonce in annonces:
        if annonce[4] > meilleure[4]:
            meilleure = annonce
    
    print(f"\nMeilleure offre : {meilleure}")
    return meilleure

def afficher_statistique(annonces):
    if len(annonces) == 0:
        print("Aucune annonce disponible")
        return
    
    nombre_total = len(annonces)
    somme_salaire = sum(annonce[4] for annonce in annonces)
    salaire_moyen = somme_salaire / nombre_total
    
    print("\n=== STATISTIQUES ===")
    print(f"Nombre total d'annonces : {nombre_total}")
    print(f"Moyenne des salaires : {salaire_moyen:.2f} DH")

def supprimer_annonces(annonces):
    id_a_supprimer = int(input("Saisir l'ID de l'annonce à supprimer : "))
    nouvelles_annonces = ()
    trouve = False
    
    for annonce in annonces:
        if annonce[0] == id_a_supprimer:
            trouve = True
            print(f"Annonce {id_a_supprimer} supprimée")
        else:
            nouvelles_annonces = nouvelles_annonces + (annonce,)
    
    if not trouve:
        print("Annonce introuvable")
        return annonces
    
    return nouvelles_annonces

annonces = () 

while True:
    print("""
    Réalisé par : Yassir KHALFOUFI.
===========================================
Système de gestion des offres d'emploi
===========================================
    1- Ajouter une annonce
    2- Afficher les annonces
    3- Rechercher une annonce
    4- Afficher la meilleure offre
    5- Afficher des statistiques
    6- Supprimer une annonce par ID
    7- Quitter
===========================================
""")
    choix = int(input("Saisir votre choix : "))
    
    if choix == 1:
        id_annonce = int(input("Identifiant de l'annonce : "))
        titre = input("Titre de l'annonce : ")
        entreprise = input("Entreprise : ")
        ville = input("Ville : ")
        salaire = int(input("Salaire : "))
        annonces = ajouter_annonces(annonces, id_annonce, titre, entreprise, ville, salaire)
        print("Annonce ajoutée avec succès!")
    
    elif choix == 2:
        afficher_annonces(annonces)
    
    elif choix == 3:
        rechercher_annonces(annonces)
    
    elif choix == 4:
        meilleur_offre(annonces)
    
    elif choix == 5:
        afficher_statistique(annonces)
    
    elif choix == 6:
        annonces = supprimer_annonces(annonces)
    
    elif choix == 7:
        print("Au revoir!")
        break
    
    else: 
        print("Choix invalide")