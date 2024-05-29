my_dict = {"key1":1,"key2":["oui",1,2,3],"key3":"Bonjour"}

print(my_dict)

print(my_dict["key2"])

for n in my_dict:
    print(n)

for i in range(1,4):
    print( i)

print("My_dict",my_dict)
print("keys",my_dict.keys())
t = zip(my_dict, range(1,4))
print(list(t))
for n,i in zip(my_dict, range(1,4)):
    print(n , i)

for n,i in zip(my_dict.keys(), range(1,4)):
    print(n , i)