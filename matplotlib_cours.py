import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = 6
dataset = {f"experience{i}": np.random.randn(100) for i in range(x)}
# On vient créer un dataset qui contient x expérience avec chacune 100 résultat basé sur la loi normale
print(dataset)

def graphique(data):
    n = len(data)
    plt.figure(figsize=(12,13),num="TEST")#figsize = largeur et hauteur en pouces
    for k, i in zip(data.keys(), range(1, n+1)):
        plt.subplot(n, 1, i)
        plt.plot(data[k])
        plt.title(k)
    plt.show()

graphique(dataset)