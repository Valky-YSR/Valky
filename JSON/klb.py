import json

FICHIER_CATALOGUE = "catalogue.json"

def charger_catalogue():
    try:
        with open(FICHIER_CATALOGUE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def sauvegarder_catalogue(catalogue):
    with open(FICHIER_CATALOGUE, 'w', encoding='utf-8') as f:
        json.dump(catalogue, f, ensure_ascii=False, indent=4)

def generer_id(catalogue):
    if not catalogue:
        return 1
    return max(produit['id'] for produit in catalogue) + 1

def ajouter_produit(catalogue):
    print("\n=== Ajouter un produit ===")
    nom = input("Nom du produit: ")
    prix = float(input("Prix: "))
    quantite = int(input("Quantite: "))
    categorie = input("Categorie: ")
    
    nouveau_produit = {
        'id': generer_id(catalogue),
        'nom': nom,
        'prix': prix,
        'quantite': quantite,
        'categorie': categorie
    }
    
    catalogue.append(nouveau_produit)
    sauvegarder_catalogue(catalogue)
    print(f"\nProduit ajoute avec succes (ID: {nouveau_produit['id']})")

def rechercher_produit(catalogue):
    print("\n=== Rechercher un produit ===")
    print("1. Rechercher par ID")
    print("2. Rechercher par nom")
    choix = input("Votre choix: ")
    
    resultats = []
    
    if choix == '1':
        id_recherche = int(input("Entrez l'ID: "))
        resultats = [p for p in catalogue if p['id'] == id_recherche]
    elif choix == '2':
        nom_recherche = input("Entrez le nom: ").lower()
        resultats = [p for p in catalogue if nom_recherche in p['nom'].lower()]
    
    if resultats:
        print("\nProduits trouves:")
        for produit in resultats:
            afficher_produit(produit)
    else:
        print("\nAucun produit trouve")
    
    return resultats

def afficher_produit(produit):
    print(f"\nID: {produit['id']}")
    print(f"Nom: {produit['nom']}")
    print(f"Prix: {produit['prix']} DH")
    print(f"Quantite: {produit['quantite']}")
    print(f"Categorie: {produit['categorie']}")
    print("-" * 30)

def modifier_produit(catalogue):
    print("\n=== Modifier un produit ===")
    id_modif = int(input("Entrez l'ID du produit a modifier: "))
    
    produit = None
    for p in catalogue:
        if p['id'] == id_modif:
            produit = p
            break
    
    if not produit:
        print("Produit introuvable")
        return
    
    print("\nProduit actuel:")
    afficher_produit(produit)
    
    print("\nLaissez vide pour conserver la valeur actuelle")
    
    nom = input(f"Nouveau nom [{produit['nom']}]: ")
    if nom:
        produit['nom'] = nom
    
    prix = input(f"Nouveau prix [{produit['prix']}]: ")
    if prix:
        produit['prix'] = float(prix)
    
    quantite = input(f"Nouvelle quantite [{produit['quantite']}]: ")
    if quantite:
        produit['quantite'] = int(quantite)
    
    categorie = input(f"Nouvelle categorie [{produit['categorie']}]: ")
    if categorie:
        produit['categorie'] = categorie
    
    sauvegarder_catalogue(catalogue)
    print("\nProduit modifie avec succes")

def supprimer_produit(catalogue):
    print("\n=== Supprimer un produit ===")
    id_suppr = int(input("Entrez l'ID du produit a supprimer: "))
    
    for i, p in enumerate(catalogue):
        if p['id'] == id_suppr:
            afficher_produit(p)
            confirmation = input("Confirmer la suppression? (oui/non): ")
            if confirmation.lower() == 'oui':
                catalogue.pop(i)
                sauvegarder_catalogue(catalogue)
                print("Produit supprime avec succes")
            else:
                print("Suppression annulee")
            return
    
    print("Produit introuvable")

def afficher_tous_produits(catalogue):
    if not catalogue:
        print("\nLe catalogue est vide")
        return
    
    print("\n=== Liste des produits ===")
    for produit in catalogue:
        afficher_produit(produit)

def afficher_menu():
    print("\n" + "="*40)
    print("GESTION DE CATALOGUE DE PRODUITS")
    print("="*40)
    print("1. Ajouter un produit")
    print("2. Rechercher un produit")
    print("3. Modifier un produit")
    print("4. Supprimer un produit")
    print("5. Afficher tous les produits")
    print("6. Quitter")
    print("="*40)

def main():
    catalogue = charger_catalogue()
    
    while True:
        afficher_menu()
        choix = input("\nVotre choix: ")
        
        if choix == '1':
            ajouter_produit(catalogue)
        elif choix == '2':
            rechercher_produit(catalogue)
        elif choix == '3':
            modifier_produit(catalogue)
        elif choix == '4':
            supprimer_produit(catalogue)
        elif choix == '5':
            afficher_tous_produits(catalogue)
        elif choix == '6':
            print("\nAu revoir!")
            break
        else:
            print("\nChoix invalide")

if __name__ == "__main__":
    main()