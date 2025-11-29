import csv
import os

FICHIER = 'inventaire.csv'
CHAMPS = ['Code', 'Nom', 'Catégorie', 'Quantité', 'PrixUnitaire']

# ---------------------------------------------------------
# 1. Création du fichier CSV s'il n'existe pas
# ---------------------------------------------------------
if not os.path.exists(FICHIER):
    with open(FICHIER, 'w', newline='', encoding='utf-8') as f:
        ecrivain = csv.writer(f)
        ecrivain.writerow(CHAMPS)  # écrire l'en-tête

# ---------------------------------------------------------
# 2. Ajouter un produit
# ---------------------------------------------------------
def ajouter_produit():
    code = input("Code : ").strip()
    nom = input("Nom : ").strip()
    cat = input("Catégorie : ").strip()
    quantite = input("Quantité : ").strip()
    prix = input("PrixUnitaire : ").strip()
    with open('inventaire.csv', 'a', newline='', encoding='utf-8') as f:
        ecrivain = csv.writer(f)
        ecrivain.writerow([code, nom, cat, quantite, prix])
    print("Produit ajouté.\n")

# ---------------------------------------------------------
# 3. Afficher tous les produits
# ---------------------------------------------------------
def afficher_inventaire():
    with open(FICHIER, newline='', encoding='utf-8') as f:
        lecteur = csv.DictReader(f)
        print("\n=== Inventaire ===")
        for ligne in lecteur:
            print(f"{ligne['Code']} - {ligne['Nom']} - {ligne['Catégorie']} - {ligne['Quantité']} - {ligne['PrixUnitaire']}")
        print("----------------\n")

# ---------------------------------------------------------
# 4. Modifier un produit
# ---------------------------------------------------------
def modifier_produit():
    code_mod = input("Code du produit à modifier : ").strip()
    produits = []
    with open(FICHIER, newline='', encoding='utf-8') as f:
        lecteur = csv.DictReader(f)
        for ligne in lecteur:
            if ligne['Code'] == code_mod:
                print("Laisser vide pour ne pas modifier")
                ligne['Nom'] = input(f"Nom ({ligne['Nom']}) : ") or ligne['Nom']
                ligne['Catégorie'] = input(f"Catégorie ({ligne['Catégorie']}) : ") or ligne['Catégorie']
                quantite = input(f"Quantité ({ligne['Quantité']}) : ").strip()
                prix = input(f"PrixUnitaire ({ligne['PrixUnitaire']}) : ").strip()
                if quantite: ligne['Quantité'] = quantite
                if prix: ligne['PrixUnitaire'] = prix
            produits.append(ligne)
    with open(FICHIER, 'w', newline='', encoding='utf-8') as f:
        ecrivain = csv.DictWriter(f, fieldnames=CHAMPS)
        ecrivain.writeheader()
        ecrivain.writerows(produits)
    print("Produit modifié.\n")

# ---------------------------------------------------------
# 5. Supprimer un produit
# ---------------------------------------------------------
def supprimer_produit():
    code_sup = input("Code du produit à supprimer : ").strip()
    produits = []
    with open(FICHIER, newline='', encoding='utf-8') as f:
        lecteur = csv.DictReader(f)
        for ligne in lecteur:
            if ligne['Code'] != code_sup:
                produits.append(ligne)
    with open(FICHIER, 'w', newline='', encoding='utf-8') as f:
        ecrivain = csv.DictWriter(f, fieldnames=CHAMPS)
        ecrivain.writeheader()
        ecrivain.writerows(produits)
    print("Produit supprimé.\n")

# ---------------------------------------------------------
# 6. Rechercher par Nom ou Catégorie
# ---------------------------------------------------------
def rechercher_produit():
    choix = input("Rechercher par (1) Nom ou (2) Catégorie ? ")
    critere = input("Entrer le critère : ").strip().lower()
    with open(FICHIER, newline='', encoding='utf-8') as f:
        lecteur = csv.DictReader(f)
        trouve = False
        for ligne in lecteur:
            if (choix == '1' and critere in ligne['Nom'].lower()) or \
               (choix == '2' and critere in ligne['Catégorie'].lower()):
                print(f"{ligne['Code']} - {ligne['Nom']} - {ligne['Catégorie']} - {ligne['Quantité']} - {ligne['PrixUnitaire']}")
                trouve = True
        if not trouve:
            print("Aucun produit trouvé.\n")

# ---------------------------------------------------------
# 7. Calculer valeur totale du stock
# ---------------------------------------------------------
def valeur_stock():
    total = 0
    with open(FICHIER, newline='', encoding='utf-8') as f:
        lecteur = csv.DictReader(f)
        for ligne in lecteur:
            total += int(ligne['Quantité']) * float(ligne['PrixUnitaire'])
    print(f"Valeur totale du stock : {total}\n")

# ---------------------------------------------------------
# Menu principal
# ---------------------------------------------------------
def menu():
    while True:
        print("=== Gestion Inventaire CSV ===")
        print("1. Afficher inventaire")
        print("2. Ajouter produit")
        print("3. Modifier produit")
        print("4. Supprimer produit")
        print("5. Rechercher produit")
        print("6. Valeur totale du stock")
        print("7. Quitter")
        choix = input("Votre choix : ").strip()
        if choix == '1': afficher_inventaire()
        elif choix == '2': ajouter_produit()
        elif choix == '3': modifier_produit()
        elif choix == '4': supprimer_produit()
        elif choix == '5': rechercher_produit()
        elif choix == '6': valeur_stock()
        elif choix == '7': break
        else: print("Choix invalide.\n")

if __name__ == "__main__":
    menu()