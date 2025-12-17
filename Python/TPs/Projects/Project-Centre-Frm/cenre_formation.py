les_apprenants = {}
les_formateurs = {}
les_modules = {}
les_salles = {}
les_seances = {}

def ajouter(id_apprenant,nom_appr,id_formateur,nom_formateur,id_module,nom_module,id_salle,nom_salle,id_seance,nom_seance):
    choix1 = input("Entrez votre choix")
    print("""
    =====Ajouter des entrées====
    1. Ajouter un apprenant
    2. Ajouter un module
    3. Ajouter un(e) formateur
    3. Ajouter une salle
    5. Ajouter une seance
    """)
    if choix1 == "1":
        id_apprenant = input("Entrez l'ID d'apprenant : ")
        if id_apprenant in les_apprenants:
            print("Il y a deja un apprenant avec ce id.")
            return
        id_apprenant=input("Saisir un nouveau ID d'apprenant")
        nom_appr= input("Saisir le nom d'apprenant : ")

        les_apprenants[id_apprenant] = {"ID": id_apprenant,"Nom": nom_appr}
        print("L'apprenant a ete ajoute!")
    elif choix1 == "2":
        id_module = input("Entrez l'ID du module : ")
        if id_module in les_modules:
            print("Il y a deja un module avec ce id.")
            return
        id_module=input("Saisir un nouveau ID du Module")
        nom_module= input("Saisir le nom de module : ")

        les_modules[id_module] = {"ID": id_module,"Nom": nom_module}
        print("Le module a ete ajoute!")
    elif choix1 == "3":
        id_formateur = input("Entrez l'ID de formateur : ")
        if id_formateur in les_apprenants:
            print("Il y a deja un formateur avec ce id.")
            return
        id_formateur=input("Saisir un nouveau ID de formateur")
        nom_formateur= input("Saisir le nom de formateur : ")

        les_formateurs[id_formateur] = {"ID": id_formateur,"Nom": nom_formateur}
        print("Le formateur a ete ajoute!")
    elif choix1 == "4":
        id_salle = input("Entrez l'ID du salle: ")
        if id_salle in les_salles:
            print("Il y a deja une salle avec ce id.")
            return
        id_salle=input("Saisir un nouveau ID du salle")
        nom_salle= input("Saisir le nom du salle : ")

        les_salles[id_apprenant] = {"ID": id_salle,"Nom": nom_salle}
        print("L'a salle a ete ajoute!")
    elif choix1 == "5":
        id_seance = input("Entrez l'ID de seance: ")
        if id_seance in les_seances:
            print("Il y a deja une seance avec ce id.")
            return
        id_seance=input("Saisir un nouveau ID de seance")
        nom_seance= input("Saisir le nom de seance : ")
        les_seances[id_seance] = {"Seance" : {nom_seance}}
        print("La seance a ete ajoute!")

def modifier():
    print("""
    =====Modifier=====
        1. Modifier l'entree des appreanants
        2. Modiifer l'entree des formateurs
        3. Modifier l'entree des modules
        4. Modifier l'entree des salles
        5. Modifier l'entree des seances
          """)
    choix2 = input("Entrez votre choix")
    if choix2 == "1":
        id_apprenant = input("Entrez l'ID d'apprenant a modifier : ")
        if id_apprenant not in les_apprenants:
            print("Aucun apprenant trouve avec cet ID.")
            return
        nom_appr = input("Entrez le nouveau nom d'apprenant : ")
        les_apprenants[id_apprenant]["Nom"] = nom_appr
        print("L'apprenant a ete modifie!")
    elif choix2 == "2":
        id_formateur = input("Entrez l'ID de formateur a modifier : ")
        if id_formateur not in les_formateurs:
            print("Aucun formateur trouve avec cet ID.")
            return
        nom_formateur = input("Entrez le nouveau nom de formateur : ")
        les_formateurs[id_formateur]["Nom"] = nom_formateur
        print("Le formateur a ete modifie!")
    elif choix2 == "3":
        id_module = input("Entrez l'ID du module a modifier : ")
        if id_module not in les_modules:
            print("Aucun module trouve avec cet ID.")
            return
        nom_module = input("Entrez le nouveau nom de module : ")
        les_modules[id_module]["Nom"] = nom_module
        print("Le module a ete modifie!")
    elif choix2 == "4":
        id_salle = input("Entrez l'ID de salle a modifier : ")
        if id_salle not in les_salles:
            print("Aucune salle trouve avec cet ID.")
            return
        nom_salle = input("Entrez le nouveau nom de salle : ")
        les_salles[id_salle]["Nom"] = nom_salle
        print("La salle a ete modifie!")
    elif choix2 == "5":
        id_seance = input("Entrez l'ID de seance a modifier : ")
        if id_seance not in les_seances:
            print("Aucune seance trouve avec cet ID.")
            return
        nom_seance = input("Entrez le nouveau nom de seance : ")
        les_seances[id_seance]["Nom"] = nom_seance
        print("La seance a ete modifie!")
def supprimer():
    id_apprenant = input("Entrez l'ID d'apprenant a supprimer : ")
    if id_apprenant in les_apprenants:
        del les_apprenants[id_apprenant]
        print("L'apprenant a ete supprime!")
    else:
        print("Aucun apprenant trouve avec cet ID.")
def rechercher():
    print("""
    =====Rechercher=====
        1. Rechercher un apprenant
        2. Rechercher un formateur
        3. Rechercher un module
        4. Rechercher une salle
        5. Rechercher une seance
          """)
    choix3 = input("Entrez votre choix")
    if choix3 == "1":
        id_apprenant = input("Entrez l'ID d'apprenant a rechercher : ")
        if id_apprenant in les_apprenants:
            print("Apprenant trouve :", les_apprenants[id_apprenant])
        else:
            print("Aucun apprenant trouve avec cet ID.")
    elif choix3 == "2":
        id_formateur = input("Entrez l'ID de formateur a rechercher : ")
        if id_formateur in les_formateurs:
            print("Formateur trouve :", les_formateurs[id_formateur])
        else:
            print("Aucun formateur trouve avec cet ID.")
    elif choix3 == "3":
        id_module = input("Entrez l'ID du module a rechercher : ")
        if id_module in les_modules:
            print("Module trouve :", les_modules[id_module])
        else:
            print("Aucun module trouve avec cet ID.")
    elif choix3 == "4":
        id_salle = input("Entrez l'ID de salle a rechercher : ")
        if id_salle in les_salles:
            print("Salle trouvee :", les_salles[id_salle])
        else:
            print("Aucune salle trouvee avec cet ID.")
    elif choix3 == "5":
        id_seance = input("Entrez l'ID de seance a rechercher : ")
        if id_seance in les_seances:
            print("Seance trouvee :", les_seances[id_seance])
        else:
            print("Aucune seance trouvee avec cet ID.")
def afficher():
def generer_seance():
pass
while True :
    print("""
    Realise par: Yassir KHALFOUFI
    ==========Formation==========
    | 1 | Gestion des apprenants |
    | 2 | Gestion des formateurs |
    | 3 | Gestion des modules    |
    | 4 | Gestion des salles     |
    | 5 | Gestion des séances    |
    | 6 | Générer rapport final  |
    | 0 | Quitter                |
    """)
    choix = input("Entrez votre choix : ")
    if choix == "1" :
        ajouter()
    elif choix == "2" :
        modifier()
    elif choix == "3":
        supprimer()
    elif choix == "4" :
        
    elif choix == "5":
       pass
    elif choix == "6":
        pass
    elif choix == "0":
        print("Au revoir!")
        break
    else:
        print("Choix invalide. Veuille saisir un nombre entre 0 et 6")
