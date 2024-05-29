# Definition d'une fonction
def ma_fonction(var_1, var_2):
    pass
    calcul = var_1 + var_2
    if calcul < 10: # On check si inf à 10
        calcul = 0
        return "OUI OUI"
    return calcul


xy = ma_fonction(1,"Non non")
print("xy = ", xy)