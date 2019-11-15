friends = ["Faiz Alauddin"]
friends.append("Ma'ruf")
print("Isi List : ", friends)

friends.insert(1, "Darmawan")
print("List My friends : ", friends)

print()
women_friends = ["Tsniyah", "Rahmawati", "Tasya", "Rini"]
friends.extend(women_friends[0:4])
print("Gabungkan List : ", friends)

print()
friends.sort()
print("Urutkan Berdasakan abjad : ", friends)

print()
friends.reverse()
print("Reverse : ", friends)

print()
friends.remove("Alauddin")
print("Remove Mustofa :  ", friends)