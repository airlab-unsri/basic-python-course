a_list = []
a_list.append(1)
a_list.append('a string')
a_list.append(True)

print(a_list)

for element in a_list:
    print(type(element))

a_list.insert(1, 'inserted')
print(a_list)
a_list.extend(['another', 'list'])
print(a_list)
a_list.reverse()
print(a_list)
a_list.remove('inserted')
print(a_list)


# sort by data types
def sort_key(value):
    # https://stackoverflow.com/a/5008854/9157799
    return len(type(value).__name__)


a_list.sort(key=sort_key)
print(a_list)

# create 2D List using List Comprehension
list_2d = [list(range(y*10, y*10+10)) for y in list(range(10))]

print(list_2d)
