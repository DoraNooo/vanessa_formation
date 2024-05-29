from Librairie_formation import try_int  

while True : 
    age_int = try_int(input("Quel est ton âge?"))
    if age_int == False :
        print("indiquez un nombre")
        continue
    else : 
        if age_int >= 18 :
            print("majeur")
        else :
            print("mineur")
    break
    










# def try_int(age) :
#     try :
#         age_int = int(age)
#         return age_int
#     except :
#         return False


# while True : 
#     age = input("Quel est ton âge?")
#     if try_int(age) == False :
#         print("indiquez un nombre")
#         continue
#     else : 
#         age_int = int(age)
#         if age_int >= 18 :
#             print("majeur")
#         else :
#             print("mineur")
#     break

# while True : 
#     age_int = try_int(input("Quel est ton âge?"))
#     if age_int :
#         if age_int >= 18 :
#             print("majeur")
#         else :
#             print("mineur")     
#         break
#     else : 
#         print("indiquez un nombre")




# while True : 
#     age = input("Quel est ton âge?")
#     age_int = try_int(age)
#     if age_int :
#         if age_int >= 18 :
#             print("majeur")
#         else :
#             print("mineur")     
#         break
#     else : 
#         print("indiquez un nombre")