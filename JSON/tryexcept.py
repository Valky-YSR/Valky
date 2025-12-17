try:
    x = int(input("Entrez un nombre"))
    resultat =  10 / x
except ZeroDivisionError:
    print("Erreur : Division par zero")
except ValueError:
    print("Erreur : Veuillez entrer un nombre valide")
except ArithmeticError as e:
    print(f"Erreur arrithmetique : {e}")
except Exception as e:
    print(type(e))
    print(e)
else:
    print("resultat: ", resultat)
finally:
    print("Fin du bloc try-except")