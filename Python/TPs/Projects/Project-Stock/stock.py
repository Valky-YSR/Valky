stock_actuel = {"Viande","Poisson","Poulet","Bimo"}
commande_fournisseur = {"Viande","Poisson","Poulet"}
produits_perimes = {"Bimo","Danone","Fromage"}
monquant = {"Cahier","Stylo"}
produit = ["huile","riz","lait","oeufs","ble"]
stock_mis_a_jour = stock_actuel.union(commande_fournisseur)
def prod_intersection():
    print("""
====INTERSECTION====

    1. TROUVER LES PRODUITS PRESENTS EN STOCK ET LES COMMANDES
    2. TROUVER LES PRODUITS PRESENTS EN STOCK OU LES COMMANDES
""")
    choix=int(input("Trouver les produits presents en stock et les commandes"))
    if choix == 1 :
        print(stock_actuel.intersection(commande_fournisseur))
    elif choix == 2 :
        print(stock_actuel.union(commande_fournisseur))
# menu prncpl
def exclusive():   
    print("""
====Trouver====\n
  1. Uniquement en stock\n
  2. Uniquement en les commandes\ 
""")
    choix = int(input("Saisir votre choix : "))
    if choix == 1 :
        print(stock_actuel.difference(commande_fournisseur))
    elif choix == 2 :
        print(commande_fournisseur.difference(stock_actuel))

while True :
    print("""
    ============Réalisée par Yassir KHALFOUFI===============
    ====Système de gestion des produits d'un supermarché====
                1. Mise à jour du stock.
            2. Suppression des produits périmés.
            3. Détetction des produits manquants.
              4. Produits en stock et commandes.
                 5. Produits exclusives.
                      6. Quitter.
    ========================================================
    """)
    choix1=int(input("Choisissez votre choix désiré : "))
    if choix1 == 1:
        print(stock_mis_a_jour)
    elif choix1 == 2 :
        produits_perimes.clear()
        print(f"Après : {produits_perimes}")
        print("Supprimons ....")
        print("Les produits perimés ont été supprimés.")
    elif choix1 == 3 :
        print(f"Les produits monquants sont : {monquant}")
    elif choix1 == 4 :
        prod_intersection()
    elif choix1 == 5 :
        exclusive()
    elif choix1 == 6 :
        print("Au revoir ! ")
        break
    else :
        print("Choix invalide. Veuillez saisir un nombre entre 1 et 6.")

print(f"""Les operations effectues: 
Les produits perimes ont ete detectes et supprimés.
Les produits monquants ont ete detecte et sont : {monquant}
Les produits en stock et commandes sont : {stock_actuel.union(commande_fournisseur)}
Les produits exclusives sont : {stock_actuel.difference(commande_fournisseur)}

L'état final du stock est : {stock_mis_a_jour}
""")
print("""===RECOMMENDATIONS===""")
if len(stock_mis_a_jour) < 5 :
    print("Achetez plus de produits")
else :
    print("Stock suffisant, Visitez le supermarché une autre fois.")
print("Au revoir !")