# Job 1
def get_fruit():
    return ["pomme", "cerise", "orange"]
print(get_fruit())

# Job 2 
def get_fruit():
    fruits = ["pomme", "cerise", "orange"]
    return fruits
fruits = get_fruit()
print(fruits[1])

# Job 3
def get_melon():
    fruits = ["pomme", "cerise", "orange"]
    fruits.append("melon")
    return fruits
print(get_melon())

# Job 4
def get_mangue():
    fruits = ["pomme", "cerise", "orange", "melon"]
    fruits.insert(2, "mangue")
    return fruits
print(get_mangue())

# Job 5 
L = [1, 2, 3, 4, 5]
def remplacer_3(L):
    if len(L) >= 5:
        L[3] = L[2] + L[4]
    return L
print("Liste avant modification:", L)
L = remplacer_3(L)
print("Deuxième valeur de la liste:", L[1])
print("Dernière valeur de la liste:", L[-1])
print("Liste après modification:", L)

# Job 6
def echanger_premier_dernier(L):
    if len(L) > 0:
        L[0], L[-1] = L[-1], L[0]
    return L
print("Liste avant échange :", L)
L = echanger_premier_dernier(L)
print("Liste après échange :", L)

# Job 7
L = [8, 24, 48, 2, 16]
multiples_de_3 = [x for x in L if x % 3 == 0]
print("Nombre de multiples de 3 :", len(multiples_de_3))
