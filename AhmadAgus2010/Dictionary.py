buah = {}
buah["Apple"] = 20
buah["Klengkeng"] = 50
buah[1] = "rambutan"

print(buah)

#get, untuk mengambil value dengan key tertentu
#has_key, untuk memeriksa apakah dict mempunyai suatu key
#keys, mengambil key saja
#items, mengambil value saja
#update, menambah isi dict
#pop, membuang salah satu elemen berdasarkan dict
#popitem, membuang salah satu elemen
#clear, mengosongkan dict

x = {"nama":"rahmat", "kelas":"Sk reg A", "jurusan":"SK"}
y = {"zoo":"no"}

print(x.get("kelas"))

print(x.keys())
print(x.items())

x.update(y)
print(x)

x.pop("kelas")
print(x)

x.popitem()
print(x)

x.clear()
y.clear()

print(x)
print(y)