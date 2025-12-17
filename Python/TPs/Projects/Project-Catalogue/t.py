# Gestion d'un Centre de Formation
# Réalisé par: Yassir KHALFOUFI

# Dictionnaires globaux
les_apprenants = {}
les_formateurs = {}
les_modules = {}
les_salles = {}
les_seances = {}

# ============ FONCTIONS UTILITAIRES ============

def generer_id(dictionnaire):
    """Génère automatiquement un ID unique pour un dictionnaire"""
    if not dictionnaire:
        return 1
    return max(dictionnaire.keys()) + 1

def afficher_ligne():
    """Affiche une ligne de séparation"""
    print("-" * 50)

# ============ FONCTION AJOUTER ============

def ajouter(type_entree):
    """Ajoute une entrée selon le type spécifié"""
    afficher_ligne()
    
    if type_entree == "apprenant":
        id_nouveau = generer_id(les_apprenants)
        nom = input("Entrez le nom de l'apprenant : ")
        les_apprenants[id_nouveau] = nom
        print(f"✓ Apprenant ajouté avec l'ID {id_nouveau}")
        
    elif type_entree == "formateur":
        id_nouveau = generer_id(les_formateurs)
        nom = input("Entrez le nom du formateur : ")
        les_formateurs[id_nouveau] = nom
        print(f"✓ Formateur ajouté avec l'ID {id_nouveau}")
        
    elif type_entree == "module":
        id_nouveau = generer_id(les_modules)
        nom = input("Entrez le nom du module : ")
        les_modules[id_nouveau] = nom
        print(f"✓ Module ajouté avec l'ID {id_nouveau}")
        
    elif type_entree == "salle":
        id_nouveau = generer_id(les_salles)
        nom = input("Entrez le nom de la salle : ")
        les_salles[id_nouveau] = nom
        print(f"✓ Salle ajoutée avec l'ID {id_nouveau}")

# ============ FONCTION MODIFIER ============

def modifier(type_entree):
    """Modifie une entrée selon le type spécifié"""
    afficher_ligne()
    
    if type_entree == "apprenant":
        if not les_apprenants:
            print("Aucun apprenant dans la base.")
            return
        afficher("apprenant")
        id_modif = int(input("Entrez l'ID de l'apprenant à modifier : "))
        if id_modif in les_apprenants:
            nouveau_nom = input("Entrez le nouveau nom : ")
            les_apprenants[id_modif] = nouveau_nom
            print("✓ Apprenant modifié!")
        else:
            print("✗ ID introuvable.")
            
    elif type_entree == "formateur":
        if not les_formateurs:
            print("Aucun formateur dans la base.")
            return
        afficher("formateur")
        id_modif = int(input("Entrez l'ID du formateur à modifier : "))
        if id_modif in les_formateurs:
            nouveau_nom = input("Entrez le nouveau nom : ")
            les_formateurs[id_modif] = nouveau_nom
            print("✓ Formateur modifié!")
        else:
            print("✗ ID introuvable.")
            
    elif type_entree == "module":
        if not les_modules:
            print("Aucun module dans la base.")
            return
        afficher("module")
        id_modif = int(input("Entrez l'ID du module à modifier : "))
        if id_modif in les_modules:
            nouveau_nom = input("Entrez le nouveau nom : ")
            les_modules[id_modif] = nouveau_nom
            print("✓ Module modifié!")
        else:
            print("✗ ID introuvable.")
            
    elif type_entree == "salle":
        if not les_salles:
            print("Aucune salle dans la base.")
            return
        afficher("salle")
        id_modif = int(input("Entrez l'ID de la salle à modifier : "))
        if id_modif in les_salles:
            nouveau_nom = input("Entrez le nouveau nom : ")
            les_salles[id_modif] = nouveau_nom
            print("✓ Salle modifiée!")
        else:
            print("✗ ID introuvable.")
            
    elif type_entree == "seance":
        if not les_seances:
            print("Aucune séance dans la base.")
            return
        afficher("seance")
        id_modif = int(input("Entrez l'ID de la séance à modifier : "))
        if id_modif in les_seances:
            nouveau_nom = input("Entrez la nouvelle description : ")
            les_seances[id_modif] = nouveau_nom
            print("✓ Séance modifiée!")
        else:
            print("✗ ID introuvable.")

# ============ FONCTION SUPPRIMER ============

def supprimer(type_entree):
    """Supprime une entrée selon le type spécifié"""
    afficher_ligne()
    
    if type_entree == "apprenant":
        if not les_apprenants:
            print("Aucun apprenant dans la base.")
            return
        afficher("apprenant")
        id_supp = int(input("Entrez l'ID de l'apprenant à supprimer : "))
        if id_supp in les_apprenants:
            del les_apprenants[id_supp]
            print("✓ Apprenant supprimé!")
        else:
            print("✗ ID introuvable.")
            
    elif type_entree == "formateur":
        if not les_formateurs:
            print("Aucun formateur dans la base.")
            return
        afficher("formateur")
        id_supp = int(input("Entrez l'ID du formateur à supprimer : "))
        if id_supp in les_formateurs:
            del les_formateurs[id_supp]
            print("✓ Formateur supprimé!")
        else:
            print("✗ ID introuvable.")
            
    elif type_entree == "module":
        if not les_modules:
            print("Aucun module dans la base.")
            return
        afficher("module")
        id_supp = int(input("Entrez l'ID du module à supprimer : "))
        if id_supp in les_modules:
            del les_modules[id_supp]
            print("✓ Module supprimé!")
        else:
            print("✗ ID introuvable.")
            
    elif type_entree == "salle":
        if not les_salles:
            print("Aucune salle dans la base.")
            return
        afficher("salle")
        id_supp = int(input("Entrez l'ID de la salle à supprimer : "))
        if id_supp in les_salles:
            del les_salles[id_supp]
            print("✓ Salle supprimée!")
        else:
            print("✗ ID introuvable.")
            
    elif type_entree == "seance":
        if not les_seances:
            print("Aucune séance dans la base.")
            return
        afficher("seance")
        id_supp = int(input("Entrez l'ID de la séance à supprimer : "))
        if id_supp in les_seances:
            del les_seances[id_supp]
            print("✓ Séance supprimée!")
        else:
            print("✗ ID introuvable.")

# ============ FONCTION RECHERCHER ============

def rechercher(type_entree):
    """Recherche une entrée selon le type spécifié"""
    afficher_ligne()
    
    if type_entree == "apprenant":
        id_rech = int(input("Entrez l'ID de l'apprenant : "))
        if id_rech in les_apprenants:
            print(f"✓ Apprenant trouvé: ID {id_rech} | {les_apprenants[id_rech]}")
        else:
            print("✗ Introuvable")
            
    elif type_entree == "formateur":
        id_rech = int(input("Entrez l'ID du formateur : "))
        if id_rech in les_formateurs:
            print(f"✓ Formateur trouvé: ID {id_rech} | {les_formateurs[id_rech]}")
        else:
            print("✗ Introuvable")
            
    elif type_entree == "module":
        id_rech = int(input("Entrez l'ID du module : "))
        if id_rech in les_modules:
            print(f"✓ Module trouvé: ID {id_rech} | {les_modules[id_rech]}")
        else:
            print("✗ Introuvable")
            
    elif type_entree == "salle":
        id_rech = int(input("Entrez l'ID de la salle : "))
        if id_rech in les_salles:
            print(f"✓ Salle trouvée: ID {id_rech} | {les_salles[id_rech]}")
        else:
            print("✗ Introuvable")
            
    elif type_entree == "seance":
        id_rech = int(input("Entrez l'ID de la séance : "))
        if id_rech in les_seances:
            print(f"✓ Séance trouvée: ID {id_rech} | {les_seances[id_rech]}")
        else:
            print("✗ Introuvable")

# ============ FONCTION AFFICHER ============

def afficher(type_entree):
    """Affiche tout le contenu d'un type d'entrée"""
    afficher_ligne()
    
    if type_entree == "apprenant":
        print("--- Liste des Apprenants ---")
        if not les_apprenants:
            print("Aucun apprenant enregistré.")
        else:
            for id_app, nom in les_apprenants.items():
                print(f"ID : {id_app} | {nom}")
                
    elif type_entree == "formateur":
        print("--- Liste des Formateurs ---")
        if not les_formateurs:
            print("Aucun formateur enregistré.")
        else:
            for id_form, nom in les_formateurs.items():
                print(f"ID : {id_form} | {nom}")
                
    elif type_entree == "module":
        print("--- Liste des Modules ---")
        if not les_modules:
            print("Aucun module enregistré.")
        else:
            for id_mod, nom in les_modules.items():
                print(f"ID : {id_mod} | {nom}")
                
    elif type_entree == "salle":
        print("--- Liste des Salles ---")
        if not les_salles:
            print("Aucune salle enregistrée.")
        else:
            for id_salle, nom in les_salles.items():
                print(f"ID : {id_salle} | {nom}")
                
    elif type_entree == "seance":
        print("--- Liste des Séances ---")
        if not les_seances:
            print("Aucune séance enregistrée.")
        else:
            for id_seance, description in les_seances.items():
                print(f"ID : {id_seance} | {description}")

# ============ FONCTION GENERER SEANCE ============

def generer_seance():
    """Génère une nouvelle séance en combinant module, formateur et salle"""
    afficher_ligne()
    print("=== Générer une nouvelle séance ===\n")
    
    # Vérifier que tous les éléments nécessaires existent
    if not les_modules:
        print("✗ Aucun module disponible. Veuillez d'abord ajouter des modules.")
        return
    if not les_formateurs:
        print("✗ Aucun formateur disponible. Veuillez d'abord ajouter des formateurs.")
        return
    if not les_salles:
        print("✗ Aucune salle disponible. Veuillez d'abord ajouter des salles.")
        return
    
    # Afficher les options disponibles
    print("Modules disponibles:")
    afficher("module")
    id_module = int(input("\nEntrez l'ID du module : "))
    if id_module not in les_modules:
        print("✗ Module introuvable.")
        return
    
    print("\nFormateurs disponibles:")
    afficher("formateur")
    id_formateur = int(input("\nEntrez l'ID du formateur : "))
    if id_formateur not in les_formateurs:
        print("✗ Formateur introuvable.")
        return
    
    print("\nSalles disponibles:")
    afficher("salle")
    id_salle = int(input("\nEntrez l'ID de la salle : "))
    if id_salle not in les_salles:
        print("✗ Salle introuvable.")
        return
    
    date = input("Entrez la date (optionnel, format JJ/MM/AAAA) : ")
    id_nouveau = generer_id(les_seances)
    description = f"Séance : {les_modules[id_module]} | Formateur : {les_formateurs[id_formateur]} | Salle : {les_salles[id_salle]}"
    if date:
        description += f" | Date : {date}"
    
    les_seances[id_nouveau] = description
    print(f"\n✓ Séance créée avec l'ID {id_nouveau}")
    print(f"   {description}")

def generer_rapport():
    """Génère un rapport complet de tous les éléments"""
    print("\n" + "=" * 60)
    print("        RAPPORT FINAL - CENTRE DE FORMATION")
    print("=" * 60 + "\n")
    
    afficher("apprenant")
    print()
    afficher("formateur")
    print()
    afficher("module")
    print()
    afficher("salle")
    print()
    afficher("seance")
    print("\n" + "=" * 60)

def sous_menu_gestion(type_entree, titre):
    """Affiche un sous-menu de gestion pour un type d'entrée"""
    while True:
        afficher_ligne()
        print(f"=== Gestion des {titre} ===")
        print("1. Ajouter")
        print("2. Modifier")
        print("3. Supprimer")
        print("4. Rechercher")
        print("5. Afficher tout")
        print("0. Retour")
        afficher_ligne()
        
        choix = input("Votre choix : ")
        
        if choix == "1":
            ajouter(type_entree)
        elif choix == "2":
            modifier(type_entree)
        elif choix == "3":
            supprimer(type_entree)
        elif choix == "4":
            rechercher(type_entree)
        elif choix == "5":
            afficher(type_entree)
        elif choix == "0":
            break
        else:
            print("✗ Choix invalide!")
        
        input("\nAppuyez sur Entrée pour continuer...")

def menu_principal():
    """Affiche et gère le menu principal"""
    while True:
        print("\n" + "=" * 60)
        print("        Réalisé par: Yassir KHALFOUFI")
        print("=" * 60)
        print("           GESTION CENTRE DE FORMATION")
        print("=" * 60)
        print("| 1 | Gestion des apprenants")
        print("| 2 | Gestion des formateurs")
        print("| 3 | Gestion des modules")
        print("| 4 | Gestion des salles")
        print("| 5 | Gestion des séances")
        print("| 6 | Générer une séance")
        print("| 7 | Générer rapport final")
        print("| 0 | Quitter")
        print("=" * 60)
        
        choix = input("Votre choix : ")
        
        if choix == "1":
            sous_menu_gestion("apprenant", "Apprenants")
        elif choix == "2":
            sous_menu_gestion("formateur", "Formateurs")
        elif choix == "3":
            sous_menu_gestion("module", "Modules")
        elif choix == "4":
            sous_menu_gestion("salle", "Salles")
        elif choix == "5":
            sous_menu_gestion("seance", "Séances")
        elif choix == "6":
            generer_seance()
            input("\nAppuyez sur Entrée pour continuer...")
        elif choix == "7":
            generer_rapport()
            input("\nAppuyez sur Entrée pour continuer...")
        elif choix == "0":
            print("\n" + "=" * 60)
            print("   Merci d'avoir utilisé le système de gestion!")
            print("=" * 60)
            break
        else:
            print("✗ Choix invalide! Veuillez saisir un nombre entre 0 et 7.")

if __name__ == "__main__":
    menu_principal()