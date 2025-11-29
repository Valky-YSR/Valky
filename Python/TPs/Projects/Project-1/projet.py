print("Realisé par Yassir KHALFOUFI")
# 1. Fonctions d'analyse
def compter_caracteres(texte):
    avec_espaces = len(texte)
    sans_espaces = len(texte.replace(" ", ""))
    return avec_espaces, sans_espaces

def compter_mots(texte):
    mots = texte.split()
    return len(mots), mots

def compter_voyelles_consonnes(texte):
    voyelles = "aeiouàâäéèêëïîôùûüÿæœAEIOUÀÂÄÉÈÊËÏÎÔÙÛÜŸÆŒ"
    consonnes_lettres = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZçÇ"
    nb_voyelles = sum(1 for c in texte if c in voyelles)
    nb_consonnes = sum(1 for c in texte if c in consonnes_lettres)
    return nb_voyelles, nb_consonnes

def compter_phrases(texte):
    return texte.count('.') + texte.count('!') + texte.count('?')

def trouver_mot_plus_long_court(texte):
    mots = texte.split()
    if not mots:
        return None, None
    mot_plus_long = max(mots, key=len)
    mot_plus_court = min(mots, key=len)
    return mot_plus_long, mot_plus_court

def calculer_longueur_moyenne_mots(texte):
    mots = texte.split()
    if not mots:
        return 0
    total_lettres = sum(len(mot) for mot in mots)
    return total_lettres / len(mots)

# 2. Recherche et manipulation
def trouver_occurrences(texte, element):
    premiere = texte.find(element)
    derniere = texte.rfind(element)
    nb_total = texte.count(element)
    return premiere, derniere, nb_total

def verifier_presence(texte, element):
    return "Présent" if element in texte else "Non présent"

def remplacer_mot(texte, ancien, nouveau):
    return texte.replace(ancien, nouveau)

# 3. Affichage statistiques
def afficher_stats(texte):
    avec_espaces, sans_espaces = compter_caracteres(texte)
    nb_mots, mots = compter_mots(texte)
    nb_voyelles, nb_consonnes = compter_voyelles_consonnes(texte)
    nb_phrases = compter_phrases(texte)
    mot_long, mot_court = trouver_mot_plus_long_court(texte)
    moyenne = calculer_longueur_moyenne_mots(texte)
    
    print("\n===== STATISTIQUES =====")
    print(f"Caractères (avec espaces) : {avec_espaces}")
    print(f"Caractères (sans espaces) : {sans_espaces}")
    print(f"Nombre de mots : {nb_mots}")
    print(f"Voyelles : {nb_voyelles}")
    print(f"Consonnes : {nb_consonnes}")
    print(f"Phrases : {nb_phrases}")
    print(f"Mot le plus long : {mot_long}")
    print(f"Mot le plus court : {mot_court}")
    print(f"Longueur moyenne des mots : {moyenne:.2f}")

# Programme principal
texte = input("Entrez votre texte : ")

while True:
    print("\n===== MENU =====")
    print("1. Stats")
    print("2. Rechercher")
    print("3. Vérifier présence")
    print("4. Remplacer")
    print("0. Quitter")
    
    choix = input("Votre choix : ")
    
    if choix == "1":
        afficher_stats(texte)
        
    elif choix == "2":
        element = input("Mot ou caractère à rechercher : ")
        premiere, derniere, nb_total = trouver_occurrences(texte, element)
        if premiere == -1:
            print(f"'{element}' non trouvé")
        else:
            print(f"Première occurrence : {premiere}")
            print(f"Dernière occurrence : {derniere}")
            print(f"Nombre total : {nb_total}")
            
    elif choix == "3":
        element = input("Mot ou caractère à vérifier : ")
        print(verifier_presence(texte, element))
        
    elif choix == "4":
        ancien = input("Mot à remplacer : ")
        nouveau = input("Par : ")
        texte_modifie = remplacer_mot(texte, ancien, nouveau)
        print("\nAVANT :", texte)
        print("APRÈS :", texte_modifie)
        if input("Garder les changements ? (o/n) : ").lower() == 'o':
            texte = texte_modifie
            print("Texte mis à jour !")
            
    elif choix == "0":
        print("Au revoir !")
        break
        
    else:
        print("Choix invalide !")
