import csv
import os
# les fonctions utileses

def lire_csv(nom_fichier):
    if not os.path.exists(nom_fichier):
        print(f"Le fichier {nom_fichier} n'existe pas.\n")
        return
    
    ventes = {}
    with open(nom_fichier, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            produit = row['produit']
            quantite = int(row['quantite'])
            prix = float(row['prix'])
            if produit not in ventes:
                ventes[produit] = {'quantite': 0, 'total': 0.0}
            ventes[produit]['quantite'] += quantite
            ventes[produit]['total'] += quantite * prix
    print("\nAnalyse des ventes:")
    print("====================")
    for produit, data in ventes.items():
        print("=================================")
        print(f"|---Produit: {produit}")
        print(f"|---prix unitaire: {data['total'] / data['quantite']:.2f} DHs")
        print(f"|---Quantité vendue: {data['quantite']}")
        print(f"|---Chiffre d'affaires: {data['total']:.2f} DHs\n")
        print("=================================")
    print("Analyse terminée.\n")

def Calculer_le_chiffre_daffaires_total(ventes):
    chiffre_affaires_total = sum(data['total'] for data in ventes.values())
    return chiffre_affaires_total

def generer_rapport(ventes, nom_fichier="rapport_ventes.txt"):
    with open(nom_fichier, 'w', encoding='utf-8') as f:
        f.write("Rapport de Ventes\n")
        f.write("=================\n\n")
        for produit, data in ventes.items():
            f.write(f"Produit: {produit}\n")
            f.write(f"Prix unitaire: {data['total'] / data['quantite']:.2f} DHs\n")
            f.write(f"Quantité vendue: {data['quantite']}\n")
            f.write(f"Chiffre d'affaires: {data['total']:.2f} DHs\n")
            f.write("-------------------------\n")
    print(f"\nLe rapport de ventes a été généré dans le fichier {nom_fichier}.\n")

def Trouver_le_produit_le_plus_vendu(ventes):
    produit_plus_vendu = max(ventes.items(), key=lambda item: item[1]['quantite'])
    return produit_plus_vendu

# Menu Principale
while True:
    print("""
    Réalisée par Yassir KHALFOUFI & Badreddine EJJEBLI
    ==================================================
                Analyse de ventes simple
    ==================================================
    | 1 | Analyser un fichier CSV.
    | 0 | Quitter.
    ==================================================
    """)
    choix = int(input("Choisissez une option (0-1): "))
    if choix == 1:
        nom_fichier = input("Entrez le nom du fichier CSV à analyser: ")
        if os.path.exists(nom_fichier):
            print(f"Le fichier {nom_fichier} a été trouvé.\n")
        else:
            print(f"Le fichier {nom_fichier} n'existe pas. Veuillez réessayer.\n")
            continue
        while True:
            print("""
    ============================================
             --- Options d'analyse ---
    ============================================
    | 1 | Analyse des ventes
    | 2 | Calculer le chiffre d'affaires total
    | 3 | Trouver le produit le plus vendu
    | 4 | Générer un rapport texte des ventes
    | 5 | Retour au menu principal
    ============================================""")
            choix  = int(input("Choisissez une option (1-5): "))
            if choix == 1:
                lire_csv(nom_fichier)
            elif choix == 2:
                ventes = {}
                if os.path.exists(nom_fichier):
                    with open(nom_fichier, 'r', encoding='utf-8') as f:
                        reader = csv.DictReader(f)
                        for row in reader:
                            produit = row['produit']
                            quantite = int(row['quantite'])
                            prix = float(row['prix'])
                            if produit not in ventes:
                                ventes[produit] = {'quantite': 0, 'total': 0.0}
                            ventes[produit]['quantite'] += quantite
                            ventes[produit]['total'] += quantite * prix
                    chiffre_affaires_total = Calculer_le_chiffre_daffaires_total(ventes)
                    print(f"\nLe chiffre d’affaires total est de: {chiffre_affaires_total:.2f} DHs\n")
                else:
                    print(f"Le fichier {nom_fichier} n'existe pas.\n")
            elif choix == 3:
                ventes = {}
                if os.path.exists(nom_fichier):
                    with open(nom_fichier, 'r', encoding='utf-8') as f:
                        reader = csv.DictReader(f)
                        for row in reader:
                            produit = row['produit']
                            quantite = int(row['quantite'])
                            prix = float(row['prix'])
                            if produit not in ventes:
                                ventes[produit] = {'quantite': 0, 'total': 0.0}
                            ventes[produit]['quantite'] += quantite
                            ventes[produit]['total'] += quantite * prix
                    produit_plus_vendu, data = Trouver_le_produit_le_plus_vendu(ventes)
                    print(f"\nLe produit le plus vendu est: {produit_plus_vendu} avec {data['quantite']} unités vendues.\n")
                else:
                    print(f"Le fichier {nom_fichier} n'existe pas.\n")
            elif choix == 4:
                ventes = {}
                if os.path.exists(nom_fichier):
                    with open(nom_fichier, 'r', encoding='utf-8') as f:
                        reader = csv.DictReader(f)
                        for row in reader:
                            produit = row['produit']
                            quantite = int(row['quantite'])
                            prix = float(row['prix'])
                            if produit not in ventes:
                                ventes[produit] = {'quantite': 0, 'total': 0.0}
                            ventes[produit]['quantite'] += quantite
                            ventes[produit]['total'] += quantite * prix
                    generer_rapport(ventes)
                else:
                    print(f"Le fichier {nom_fichier} n'existe pas.\n")
            elif choix == 5:
                break
    elif choix == 2:
        generer_rapport({})
    elif choix == 4:
        nom_fichier = input("Entrez le nom du fichier CSV à analyser pour calculer le chiffre d’affaires: ")
        ventes = {}
        if os.path.exists(nom_fichier):
            with open(nom_fichier, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    produit = row['produit']
                    quantite = int(row['quantite'])
                    prix = float(row['prix'])
                    if produit not in ventes:
                        ventes[produit] = {'quantite': 0, 'total': 0.0}
                    ventes[produit]['quantite'] += quantite
                    ventes[produit]['total'] += quantite * prix
            chiffre_affaires_total = Calculer_le_chiffre_daffaires_total(ventes)
            print(f"\nLe chiffre d’affaires total est de: {chiffre_affaires_total:.2f} €\n")
        else:
            print(f"Le fichier {nom_fichier} n'existe pas.\n")
    elif choix == 0:
        print("Au revoir!")
        break
    else:
        print("Option invalide. Veuillez réessayer.\n")