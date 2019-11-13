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
### IF Statement
```python
def tebaknama(name):
    nama = input("Siapa Kamu : ")
    if (nama == "Ahmad"):
        print("Saya Ahmad")
    elif (nama == "Agus" ):
        print("Saya Agus")
    else:
        print("Saya Temen nya Hasan")

tebaknama("zzzzz")
```
## Looping
### For
```python
def testLooping():
    for a in range (0,5,+1):
        print("nilai a : ", a+1)
 
testLooping()
```

### While
```python
def whileLoop():
    i = 1
    while i < 6:
        print("*_* " + " -_-")
        i+=1

whileLoop()
```


