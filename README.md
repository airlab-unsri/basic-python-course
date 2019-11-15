# basic-python-course

## Week 1

### How to print to standard output

```python
print('what to print')
```

### How to write comments

#### Single Line

```python
# this is a single line comment.
```

#### Multi Line

```python
'''
this is a multiline
comment.
'''
```

### How to declare variables

```python
a = 'ini String menggunakan tanda petik satu'    # declare a string variable
b = 123                                          # an integer
c = True                                         # a boolean
d = "String Menggunakan Tanda Petik dua"         # declare a string variable menggunakaan tanda ("") petik dua  
e = False                                        # a boolean
f = 3.5                                          # a float
g = 2+3j                                         # a complex
h = [1, 2, 3, 4, 5]                              # a list
i = ("w","o","r","l","d")                        # a tuple
# a dictionary
j = {
    "zoo": 1,
    "zii": 999,
    "zkk": {
        "will":[20, 30, 40],
        "sit": "dolar",
        "amet": {
            "zoo":1,
            "zii":2
        }
    }
}

print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
print(d)
print(type(d))
print(e)
print(type(e))
print(f)
print(type(f))
print(g)
print(type(g))
print(h)
print(type(h))
print(i)
print(type(i))
print(j)
print(type(j))
```

### User Input
```python
name = input("Masukkan Nama : ")
print("Hello " +name+ " Selamat datang")
```

### Kondisi IF
```python
nilai = input("Masukkan nilai : ")
nilai1 = int(nilai)
if nilai1 > 80:
    print("Selamat, Kamu dapat nilai A")
elif (nilai1 > 70 and nilai1 <=80):
    print("Selamat, kamu dapat nilai B")
elif nilai1 > 60 and nilai1 <= 70:
    print("selamat, kamu dapat nilai C")
elif (nilai1 > 45 and nilai1 <= 60):
    print("Selamat, kamu dapat nilai D")
else:
    print("Maaf, Kamu dapat nilai E. Kamu harus ikut ujian Remedial")
```

### Kondisi IF bersarang
```python
nilai = input("Masukkan nilai : ")
nilai1 = int(nilai)
if nilai1 > 80:
    print("Selamat, Kamu dapat nilai A")
    if nilai1 >95 and nilai1 <100:
        print("selamat, kamu dapat voucher pendidikan karena nilai kamu A")
    if nilai1 == 100:
        print("Selamat, kamu dapat kuliah gratis")
elif (nilai1 > 70 and nilai1 <=80):
    print("Selamat, kamu dapat nilai B")
elif nilai1 > 60 and nilai1 <= 70:
    print("selamat, kamu dapat nilai C")
elif (nilai1 > 45 and nilai1 <= 60):
    print("Selamat, kamu dapat nilai D")
else:
    print("Maaf, Kamu dapat nilai E. Kamu harus ikut ujian Remedial")
```

### Ternary Operator
```python
a = 100
harga = True if a > 50 else False
print(harga)

b = 50 
harga = True if b > 100 else False
print(harga)

c= 30 
harga = True if c > 10 else False
print(harga) 
```

## Looping
### Perulangan For Array
```python
a = [1, 2, 3, 4, 5]
b = ("a", "b", "c", 6, "d", "e")
c = ({"nama":"Ahmad Agus"}, {"NIM":"09021181722076"}, {"jurusan":"Teknik Inforamtika"})
d = " List Tuple Dictionary"

for test in a:
    print(test)

for test in b:
    print(test)
for test in c:
    print(test)
for test in d:
    print(test)
```

### Perulangan For 
```python
print("perulangan Menaik : ")
for i in range(0,10):
    print(i)

print("Perulangan menurun : ")
for i in range(10,0,-1):
    print(i)

print("cetak perulangan genap < 20 : ")
for i in range(2,20,+2):
    print(i)

print("cetak perulangan kelipatan 5 yang < 50 :  ")
for i in range(5,50,+5):
    print(i)
```

### Perulangan While
```python
i = 0
while i < 10:
    print("*_* " + " -_-")
    i=i+1
```