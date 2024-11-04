# Job 1
def My_prints_hello(): # Crée une fonction qui imprime "Hello World"
    print ("Hello World")

# Job 2
def My_print_name(Name): # Crée une fonction qui imprime "
    print (Name)
My_print_name("Alice") # Appelle la fonction pour imprimer "Alice"
My_print_name("Bob")
My_print_name("Charlie")
My_print_name("Diane")

# Job 3
def add(num1, num2): # Crée une fonction qui additionne deux nombres
    somme = num1 + num2 # Calcul la somme
    print(f"La somme de {num1} et {num2} est {somme}") # Imprime la somme
add(3, 5) # Appelle la fonction pour additionner 3 et 5
add(10, 20)
add(7, 8)
add(15, 25)

# Job 4
def GetHello(): # Crée une fonction qui renvoie "Hello World"
    return "Hello la Plateforme"
message = GetHello() # Appelle la fonction pour stocker le résultat dans la variable "message"
print(message) # Imprime le résultat

# Job 5
def calcule(num1, operator, num2): # Crée une fonction qui additionne deux nombres et renvoie la somme
    if operator == "+": # Vérifie si l'opérateur est "+"
        return num1 + num2 # Retourne la somme
    elif operator == "-": # Vérifie si l'opérateur est "-"
        return num1 - num2 # Retourne la différence
    elif operator == "*": # Vérifie si l'opérateur est "*"
        return num1 * num2 # Retourne le produit
    elif operator == "/": # Vérifie si l'opérateur est "/"
        return num1 / num2 # Retourne
    elif operator == "%": # Vérifie si l'opérateur est
        return num1 % num2 # Retourne
    else:
            return "Opérateur invalide"
print(calcule(10, "+", 5)) # Affiche 15
print(calcule(10, "-", 5)) # Affiche 5
print(calcule(10, "*", 5)) # Affiche 50
print(calcule(10, "/", 5)) # Affiche 2.0
print(calcule(10, "%", 5)) # Affiche 0
print(calcule(10, "^", 5)) # Affiche "Opérateur invalide"

# Job 6
def verifier_positive(nombre): # Crée une fonction qui vérifie si un nombre est positif
    if nombre > 0: # Vérifie si le nombre est supérieur à zéro
        print(f"{nombre} est positif") # Imprime "nombre est positif"
    elif nombre < 0: # Vérifie si le nombre est inférieur à zéro
        print(f"{nombre} est négatif") # Imprime "nombre est négatif"
verifier_positive(10) # Appelle la fonction pour vérifier si 10 est positif
verifier_positive(-5)
verifier_positive(0)
verifier_positive(7)
verifier_positive(-12)

# Job 7
def identifier_developpeur(language):
    if language == "JavaScript":
        print("tu es développeur web")
    elif language == "Python":
        print("tu es développeur IA")
    elif language == "Java":
        print("tu es développeur logiciel")
    elif language == "reactjs":
        print("tu es développeur mobile")
    else:
        print("un jour, je serais le meilleur développeur")

identifier_developpeur("JavaScript")
identifier_developpeur("Python")
identifier_developpeur("Java")
identifier_developpeur("reactjs")

# Job 8
def affichier_produits(type, saison):
    if type == "fruit" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruit" and saison == "été":
        print("Poire, fraise, cassis")
    elif type == "légume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "légume" and saison == "été":
        print("artichaut, aubergine, navet")
    else:
        print("Type ou saison invalide")
affichier_produits("fruit", "hivert") # Appel de la fonction
affichier_produits("fruit", "été")
affichier_produits("légume", "hivert")
affichier_produits("légume", "été")
affichier_produits("fruit", "printemps") # Exemple invalide

# Job 9
def moyenne(note1, note2, note3):
    return (note1 + note2 + note3) / 3

note1 = float(input("Saisissez la première notes : "))
note2 = float(input("Saisissez la deuxième notes : "))
note3 = float(input("Saisissez la troisième notes : "))

moyenne_etudiant = moyenne(note1, note2, note3)

if 15 <= moyenne_etudiant <= 20:
    print("Très bon élève")
elif 11 <= moyenne_etudiant < 15:
    print("bon élève")
elif 8 <= moyenne_etudiant < 11:
    print("Elève moyen")
elif 0 <= moyenne_etudiant < 8:
    print("Elève devant faires des efforts")
else: 
    print("Notes non valides")

# Job 10
# Définir la fonction pour vérifier si un nombre est pair ou impair
def est_pair_ou_impair(nombre):
    if isinstance(nombre, int) and nombre > 0:
        if nombre % 2 == 0:
            return "Le nombre est pair"
        else:
            return "Le nombre est impair"
    else:
        return "Le nombre doit être un entier positif"

# Appeler la fonction avec différents paramètres
print(est_pair_ou_impair(10))  # Affiche "Le nombre est pair"
print(est_pair_ou_impair(7))   # Affiche "Le nombre est impair"
print(est_pair_ou_impair(-3))  # Affiche "Le nombre doit être un entier positif"
print(est_pair_ou_impair(0))   # Affiche "Le nombre doit être un entier positif"

# Job 11
# Définir la fonction time_to_text
def time_to_text(minutes):
    heures = minutes // 60
    minutes_restantes = minutes % 60
    return f"{heures} heures et {minutes_restantes} minutes"

# Appeler la fonction avec différents paramètres
print(time_to_text(160))  # Affiche "2 heures et 40 minutes"
print(time_to_text(75))   # Affiche "1 heure et 15 minutes"
print(time_to_text(45))   # Affiche "0 heure et 45 minutes"

