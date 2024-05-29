import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


iris = load_iris()
print(type(iris))

# Données variables, pétale, sépale
x = iris.data
print(x)
# Les différentes classes 0 1 2
y = iris.target
names = list(iris.target_names)

print(f"x contient {x.shape[0]} examples et {x.shape[1]} variables")
print(f"il y a {np.unique(y).size} classes")

# plt.figure('Longueur et Largeur Sépal')
# # s= taille des points x[:,2 correspond à la longueur du pétal]
# plt.scatter(x[:, 0], x[:,1], c=y, alpha=0.5, s=x[:,2]*100)
# plt.xlabel('longueur sépal')
# plt.ylabel('largeur sépal')
# plt.show()

#bins = section, nombre de chandelles
plt.figure('hist')
plt.hist(x[:,0], bins=30)
plt.hist(x[:,1], bins=30)
plt.show()

plt.figure('hist2D')
plt.hist2d(x[:,0], x[:,1])
# plt.hist2d(x[:,0], x[:,1], cmap="Blues")
plt.xlabel('longueur sépal')
plt.ylabel('largeur sépal')
#Permet de quantifier les couleurs nbr d'éléments avec les deux caractéristique
plt.colorbar()
plt.show()
