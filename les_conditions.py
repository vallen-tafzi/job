# Job 1
# Demander à l'utilisateur de saisir deux valeurs
valeur1 = input("Veuillez saisir la première valeur : ")
valeur2 = input("Veuillez saisir la deuxième valeur : ")

# Comparer les deux valeurs et afficher le résultat
if valeur1 == valeur2:
    print("Valeur1 est égal à Valeur2")
else:
    print("Les deux valeurs ne sont pas égales")

# Job 2
# Initialiser la variable age
age = 20  # Remplacer 20 par l'âge souhaité

# Vérifier si la personne peut voter
if age >= 18:
    print("Tu peux voter")
else:
    print("Tu ne peux pas voter")

# Job 3
for number in range(101):  # Parcourt les nombres de 0 à 100
    if number == 26 or number == 37 or number == 88:
        continue  # Passe à l'itération suivante si le nombre est 26, 37 ou 88
    print(number)  # Affiche le nombre

# Job 4
for number in range(1, 101):  # Parcourt les nombres de 1 à 100
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# Job 5
# Fonction pour vérifier si un nombre est premier
def est_premier(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Parcourir les nombres de 2 à 1000
for number in range(2, 1001):
    if est_premier(number):
        print(number)

# Job 6
# Demander à l'utilisateur de saisir un nombre
nombre = int(input("Veuillez saisir un nombre : "))

# Vérifier si le nombre est pair ou impair et afficher le message approprié
if nombre % 2 == 0:
    print(f"Le nombre {nombre} est pair")
else:
    print(f"Le nombre {nombre} est impair")

# Job 7
# La chaîne de caractères multipliée par 10
chaine = "abcdefghijklmnopqrstuvwxyz" * 10

# Initialisation de la longueur de la sous-chaîne à afficher
longueur = 1

# Boucle pour afficher les caractères sous forme de pyramide en reprenant le début chaque fois
while longueur * (longueur + 1) // 2 <= len(chaine):
    print(chaine[:longueur])
    longueur += 1

# Job 8
# Fonction pour vérifier si un triangle peut être construit
def est_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

# Fonction pour déterminer le type de triangle
def type_triangle(a, b, c):
    if a == b == c:
        return "équilatéral"
    elif a == b or a == c or b == c:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return "rectangle et isocèle"
        else:
            return "isocèle"
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return "rectangle"
    else:
        return "quelconque"

# Demande à l'utilisateur de saisir les longueurs
a = float(input("Veuillez saisir la longueur du côté a : "))
b = float(input("Veuillez saisir la longueur du côté b : "))
c = float(input("Veuillez saisir la longueur du côté c : "))

# Vérifie si les longueurs peuvent former un triangle
if est_triangle(a, b, c):
    print(f"Les longueurs {a}, {b} et {c} peuvent former un triangle.")
    print(f"Ce triangle est {type_triangle(a, b, c)}.")
else:
    print("Les longueurs saisies ne peuvent pas former un triangle.")