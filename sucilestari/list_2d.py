list2d = []
list2d.append([])
list2d.append([])
# [ [], [] ]
#print(list2d)

list2d[0].append(1)
list2d[0].append(8)
# [ [1,8], [] ]
#print(list2d)

list2d[1].append(1)
list2d[1].append(2)
# [ [1,8], [1,2] ]
#print(list2d)

#1 | 8
#--|--
#1 | 2

for y in list2d:
    for x in y:
        print(x, end=" ")
    print()

#FIND 2D LIST DIMENSIONS
rows = len(list2d)
cols = len(list2d[0])
print("rows =",rows)
print("cols =",cols)

#ACCESSING 2D LIST BY ROW OR COLUMN
#row
row = 1
rowList = list2d[row]
print("Row list = ",rowList)

#column
col = 1
colList = []
for i in range(len(list2d)):
    colList += [ list2d[i][col]]
print("Column list = ",colList)

