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
#Input User
input("Masukkan Nilai: ")

#If-else Condition 
def test_condition():
    name = "rizki"
    
    if(name=="rizki"):
        print("this is if")
    elif(name=="rizka"):    
        print("this is elif")
    else:
        print("this is else")

#Looping for-each dan while
def test_looping():
    for x in range (0,5):
        print("nilai x: ",x)
    
    i = 0
    while (i<5):
        print("nilai i: ",i)
        i+=1
        
def test_function_return_value(input_value):
    return input_value * 2

#Global Variabel
global_var = 10
def test_namespace():
    private_var = 5
    global_var = 6

    print("private val: ", private_var)
    print("private val: ", global_var)
    
#String Operator
def test_string_operator():
    full_string = "ini string normal"
    temp_string = "string tambahan"
    upper_string = "THIS IS UPPER"
    lower_string = "this is lower"
    
    
    print(full_string + temp_string)
    print(full_string[3:6])
    print(upper_string.lower())
    print(lower_string.upper())
    print(len(full_string))
    print(full_string.strip("l"))
    print(full_string.replace("ini", "itu"))
    print(full_string.split(" "))
    
test_condition()
test_looping()
print(test_function_return_value(5))
test_string_operator()

# Membuat fungsi dengan parameter
def luas_persegipjg(panjang, lebar):
    luas = panjang * lebar
    print "Luas Persegi Panjang: %f" % luas;
luas_persegipjg(7, 4) 

# Fungsi nilai boolean  
# empty list
lis = []
print(lis,'is',bool(lis))

# empty tuple
t = ()
print(t,'is',bool(t))

# zero complex number
c = 0 + 0j
print(c,'is',bool(c))

num = 99
print(num, 'is', bool(num))

val = None
print(val,'is',bool(val))

val = True
print(val,'is',bool(val))

# empty string
str = ''
print(str,'is',bool(str))

str = 'Hello'
print(str,'is',bool(str)
