friends = ["Dwi Wahudi"]
friends.append("Mustofa")
print("Isi List : ", friends)

friends.insert(1, "Habib")
print("List My friends : ", friends)

print()
women_friends = ["Haydi", "Amanda", "Viola", "Ratih"]
friends.extend(women_friends[0:4])
print("Gabungkan List : ", friends)

print()
friends.sort()
print("Urutkan Berdasakan abjad : ", friends)

print()
friends.reverse()
print("Reverse : ", friends)

print()
friends.remove("Mustofa")
print("Remove Mustofa :  ", friends)
