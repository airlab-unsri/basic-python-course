Animal = ('bird', 'snake', 'mouse')

# This causes an error.
# TypeError: 'tuple' object does not support item assignment
# tuple[0] = 'cat'

#mengubah isi tuple harus diubah ke list dulu
t = list(Animal)
t[0] = "burung"
t[1] = "ular"
Animal = tuple(t)

print("Mengubah Isi Tuple : ", Animal)