ht = float(input("Saisir le prix hors tax total :"))
tva = 20
ttc = ht / (tva / 100 + 1)  
reduction = ttc - (ttc * 15 / 100)
if ttc >= 200 :
    print(f"Le prix total aprés le réduction est : {reduction:.2f}")
else :
    print(f"Le prix total est  : {ttc:.2f}") 
