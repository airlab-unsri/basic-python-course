list2d = []
list2d.append([])
list2d.append([])
list2d.append([])
list2d.append([])


list2d[0].append(1)
list2d[0].append(1)
list2d[0].append(1)
list2d[0].append(1)

list2d[1].append(1)
list2d[1].append("-")
list2d[1].append("-")
list2d[1].append(1)

list2d[2].append(1)
list2d[2].append("-")
list2d[2].append("-")
list2d[2].append(1)

list2d[3].append(1)
list2d[3].append(1)
list2d[3].append(1)
list2d[3].append(1)

for y in list2d:
    for x in y:
        print(x, end=" ")
    print()