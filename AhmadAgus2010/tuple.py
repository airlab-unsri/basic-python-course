my_tuple = tuple(["Hot", "Cold", "Windy"])

print("Suhu : ", my_tuple)
# list berisi angka
a = (1, 2, 3, 4, 5)

# Tuple berisi karakter dan string
b = ('a', 'b', 'c', 'd')
c = ('Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat')

# Tuple berisi list, tuple, dan dictionary
d = ([1, 2, 3], [1, 2, 3], [1, 2, 3])
e = ((1, 2, 3), (1, 2, 3), (1, 2, 3))
f = ({'a':1, 'b':2, 'c':3},{'a':2, 'b':3, 'c':4},{'a':3, 'b':4, 'c':5})

# Tuple campuran
g = (1, 'b', 2, 'Hot', [1, 2, 3], (1, 2, 3), {'Cold':1, 'Windy':2})

print ("Tuple Angka : ", a)
print ("Tuple Karakter : ", b)
print ("Tuple String : ", c)
print ("Tuple berisi List : ", d)
print ("Tuple berisi Tuple : ", e)
print ("Tuple berisi Dictionary : ", f)
print ("Tuple Campuran : ", g)