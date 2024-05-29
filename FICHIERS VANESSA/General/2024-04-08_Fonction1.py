# Definition d'une fonction
def ma_fonction(var_1, var_2):
    pass
    calcul = var_1 + var_2
    if calcul < 10: # On check si inf à 10
        calcul = 0
        return "OUI OUI"
    return calcul


xy = ma_fonction(7,9)
print("xy = ", xy)

# string(str) float(float) integer(int)

a = "Bonjour"
age_int = 0
print("type age:",type(age_int))
age_str = str(age_int)
print("type age:",type(age_str))
c = a + str(age_str)
print(c)

if age_int > 5:
    if age_int > 10:
        print("ado")
    else:
        print("enfant")
elif age_int > 5:
    print("bambin")
else:
    print("Pas né")
