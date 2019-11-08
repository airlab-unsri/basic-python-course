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
a = 'some text' # declare a string variable
b = 123         # an integer
c = True        # a boolean
```
### Input User 
```python
input("Nama ku Adalah : ")
```
###Looping For
```python
def Looping():
    for i in range (1,5):
        print("nilai i : ", i)      
testLooping()
```
### Global Variabel
```python
globalVar = 5
def testName():
    privateVar = 1
    globalVar = 2

    print("Privat Variable : ", privateVar)
    print("Global Variable : ", globalVar)

testName()
print("Global Variable 2 : ", globalVar)
```
### String Operator
```python
def testStringOperator():
    fullString = "this is full string"
    tempString = "temp string"
    upperString = "THIS IS UPPER"
    lowerString = "this is lower"

    print(fullString + tempString) #concanation
    print(fullString[3:7]) #print karakter antara kurang dari 3 dan kurang dari 7
    print(upperString.lower())
    print(lowerString.upper())
    print("len : ", len(fullString))
    print(fullString.strip("t"))
    print(fullString.replace("full", "some"))
    print(fullString.split("is"))

testStringOperator()
```
### While Looping 
```python
def whileLoop():
    x = 1
    while x < 5:
        print(x)
        x+=1
whileLoop()
```
### Cara Membuat Fungsi pada Python
```python
def nama_fungsi():
    print "Hello ini Fungsi"
```
### Membuat fungsi dengan parameter
```python
def luas_segitiga(alas, tinggi):
    luas = (alas * tinggi) / 2
    print "Luas segitiga: %f" % luas;
luas_segitiga(4, 6) # Pemanggilan fungsi
```
### fungsi untuk menampilkan semua data
```python
def show_data():
    if len(buku) <= 0:
        print "BELUM ADA DATA"
    else:
        for indeks in range(len(buku)):
            print "[%d] %s" % (indeks, buku[indeks])
```
### fungsi untuk menambah data
```python
def insert_data():
    buku_baru = raw_input("Judul Buku: ")
    buku.append(buku_baru)
```
### fungsi untuk edit data
```python
def edit_data():
    show_data()
    indeks = input("Inputkan ID buku: ")
    if(indeks > len(buku)):
        print "ID salah"
    else:
        judul_baru = raw_input("Judul baru: ")
        buku[indeks] = judul_baru
```
### fungsi untuk menhapus data
```python
def delete_data():
    show_data()
    indeks = input("Inputkan ID buku: ")
    if(indeks > len(buku)):
        print "ID salah"
    else:
        buku.remove(buku[indeks])
```
### Fungsi Membaca File Perbaris di python
```python
# buka file
file_puisi = open("puisi.txt", "r")

# baca isi file
print file_puisi.readlines()

# tutup file
file_puisi.close()
```
