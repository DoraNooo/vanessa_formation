#Initialisation d'une liste vide
my_list = []
print(type(my_list))
print("My list =", my_list)

#Initialisation d'une liste avec 5 éléments
my_list = [3,7,"oui",True,3.9]
print(type(my_list))
print("My list =", my_list)

#Affichage du premier élément de la liste, soit l'index 0
print("Element 0:",my_list[0])

# Modification du premier element
my_list[0] = "NEW"


#Affichage de chacun des élements de la liste
# print("Début de boucle :")
# for elem in my_list:
#     print(elem)
#     if elem == 7:
#         print("TROUVE")

# print("Début de boucle avec range:")
# my_range = range(len(my_list))
# print(my_range)
# for i in range(len(my_list)):
#     print(my_list[i])

print("Début de boucle avec enumerate:")
# my_enum = enumerate(my_list)
# print(my_enum)
# for elem in my_enum:
#     print(elem)
for idx, elem in enumerate(my_list):
    print("element n:",idx,"valeur:",elem)
    if elem == 7:
        my_list[idx] = "JACKPOT"

print(my_list)