my_list = []

my_list.append(1)
my_list.append(2)
my_list.append(3)

my_list.append(("victor", "ronaldo"))

plants = {}
plants["pisang"] = 23
my_list.append(plants)

print(my_list)
print(len(my_list))

my_list = ['p','r','o','b','e']
# Output: p
print(my_list[0])
# Output: o
print(my_list[2])
# Output: e
print(my_list[4])
# Error! Only integer can be used for indexing
# my_list[4.0]
# Nested List
n_list = ["Happy", [2,0,1,5]]
# Nested indexing
# Output: a
print(n_list[0][1])    
# Output: 5
print(n_list[1][3])

# Output: e
print(my_list[-1])
# Output: p
print(my_list[-5])

my_list2 = ['p','r','o','g','r','a','m','m','e','r']
# elements 3rd to 5th
print(my_list2[2:5])
# elements beginning to 4th
print(my_list2[:-5])
# elements 6th to end
print(my_list2[5:])
# elements beginning to end
print(my_list2[:])