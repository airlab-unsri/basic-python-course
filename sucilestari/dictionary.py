class orang:
    def __init__(__args__):
        pass

Plants = {}
Plants["durian"] = 10
Plants["Rambutan"] = 30
Plants[1] = "rambutan"
suci = orang()
Plants[suci] = 1

#print(Plants["durian"])
#print(Plants["Rambutan"])
print(Plants)

plants = {}

#add three key-value data to the dictionary
plants["radish"] = 2
plants["squash"] = 4
plants["carrot"] = 7

print(plants["radish"])     #Get Syntax 1
print(plants.get("radish")) #Get Syntax 2

print("------------------")

#GETS VALUES
flowers = {}

#add 3 key-value tuples to the dictionary
flowers["rose"] = 5
flowers["sunflower"] = 3
flowers["tulip"] = 1

#Get syntax 1.
print(flowers["rose"])

#Get syntax 2.
print(flowers.get("peony"))
print(flowers.get("peony","no peony found"))


#SHOWS NONE IN THE DICTIONARY
#A value can be none
print("GET: ",flowers.get("rose"))
print("GET: ",flowers.get("lily"))


#KEY ERROR
#the dictionary has no Dahlia key!
#print(flowers["Dahlia"])

#use in.
if "sunflower" in flowers:
    print("has Sunflower")
else:
    print("No Sunflower")

#use in on nonexistent key.
if "lily" in flowers:
    print("Has lily")
else:
    print("No lily")

#FOR-LOOP
for flower in flowers:
    print(flower)