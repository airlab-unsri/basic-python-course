list2d = []
list2d.append([])
list2d.append([])
#print(list2d)
#[[], []]

list2d[0].append(1)
list2d[0].append(2)
#print(list2d)
#[[1,2], []]

list2d[1].append(3)
list2d[1].append(4)
#print(list2d)
#[[1,2], [3,4]]

for y in list2d:
    for x in y:
        print(x, end="")
        print()