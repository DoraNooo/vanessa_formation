while True : 
    age = input("Quel est ton âge?")
    try :
        age_int = int(age)
    except :
        print("indiquez un nombre")
        continue
    if age_int >= 18 :
        print("majeur")
    else :
        print("mineur")
    break