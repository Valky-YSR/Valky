score = 0
with open("quiz.txt", "r", encoding="UTF-8") as f:
    questions = f.readlines()
def q1():
    for i in range(0, len(questions), 6):
        print(questions[i])
        print(questions[i+1])
        print(questions[i+2])
        print(questions[i+3])
        reponse = input("Votre réponse (A, B ou C) : ")
        if reponse.upper() == questions[i+4].strip():
            global score
            score += 1
            print("Bonne réponse !\n")
        else:
            score -= 1
            print(f"Mauvaise réponse ! La bonne réponse était {questions[i+4].strip()}.\n")
def afficher_score():
     print(f"votre score est {score} sur 10")
while True : 
    print("""
    ============== Menu ===============\n
       1. Jouer une partie\n
       2. Voir les scores enregistrés\n
       3. Quitter le programme\n
    ===================================\n
    """)
    choix = int(input("Choisir votre choix : "))
    if choix == 1:
        nom = input("Entrez votre nom : ")
        q1()
    elif choix == 2:
        afficher_score()
    elif choix == 3:
        print("Au revoire !")
        break
    else:
        print("Choix invalide, veuillez réessayer.")