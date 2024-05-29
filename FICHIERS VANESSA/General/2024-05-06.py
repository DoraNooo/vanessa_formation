var = [1, "yes", 6, "done", 18, 3, 8, 9]
print(var)

# ajouter un élément à une liste
user = input("quoi rajouter?")
var.append(user)
print(var)

# boucle énumérate & remplacer un élément d'une liste
for idx, elem in enumerate(var):
    print("element n:", idx, "valeur:", elem)
    if elem == 6:
        var[idx] = "trouvé!"
print(var)

# boucle basique
for x in var:
    print(x)

#print("taille de la liste :", len(var))

my_range = range(0, len(var), 2)
for idx in my_range:
    print("la liste 1/2 :", var[idx])

# Enlever un élément d'une liste par rapport à son index
var.pop(3)
print(var)

# Eliminer ce qui n'est pas un entier de la liste var
var = [1, "yes", 6, "done", 18, 3, 8, 9]
from Librairie_formation import try_int 
for idx, elem in enumerate(var):
    if try_int(elem) == False:
    #if not try_int(elem):
        var.pop(idx)
print(var)

# Trier une liste sans l'écraser
var_sorted = sorted(var)
print("sorted:", var_sorted)

# Trier une liste en l'écrasant / créer une nouvelle liste
var.sort()
print("sort:", var)

