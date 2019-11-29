friends = ["Hasan", "Fahri", "Kamil", "Ahmad", "Tomi"]
for teman in friends:
    print(teman)

print()
print(friends[0])
print(friends[3])
print(friends[2])
print(friends[4])
print(friends[1])

print()
print("Asli : ", friends)
friends.reverse()
print("Reverse : ", friends)

friends.pop()
print("Pop : ", friends)
friends.append("Aisyah")
print("Append : ", friends)