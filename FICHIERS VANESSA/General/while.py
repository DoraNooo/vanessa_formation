# True and False boolean
while True:
    val = input("Rentrez un nombre svp : ")
    try:
        val = int(val)
        break
    except:
        print("ATTENTION, rentrez un nombre")

print("Val:",val)
