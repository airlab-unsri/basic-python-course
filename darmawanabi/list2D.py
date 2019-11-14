list2d = []
list2d.append([])
list2d.append([])

list2d[0].append(1)
list2d[0].append(2)

list2d[1].append("Darmawan")
list2d[1].append("Abinugroho")

for y in list2d:
    for x in y:
        print(x, end=" ")
    print()
