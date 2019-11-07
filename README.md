# Basic-python-course

## Week 1

### How to print to standard output

```python
print('what to print')
```
- output :<br> 
what to print

### How to write comments

### Single Line

```python
# this is a single line comment.
```

### Multi Line

```python
'''
this is a multiline
comment.
'''
```

### How to declare variables

```python
a = 'some text'    # declare a string variable
b = 123            # an integer
c = True           # a boolean
d = "hello world"  # declare a string variable menggunakaan tanda ("") petik dua  
e = false          # a boolean
f = 3.5            # a float
g = 2+3j           # a complex
h = [1,2,3,4]      # a list
i = ("w","o","r","l","d") # a tuple

```
### Conditional

```python
def test_conditional():
    nama = "wenty"

    if(nama == "wenty"):
        print ("this is if")
    elif (nama == "tiara"):
        print ("this is elif")
    else:
        print("else")

test_conditional()
```
- output :<br> 
this is if

### How to Looping

```python
def test_looping():
    for x in range (0,5):
        print("nilai x:",x)

    i = 0
    while (i<5):
        print ("nilai i:",i)
        i += 1

test_looping()
```
- output : <br>
nilai x: 0<br>
nilai x: 1<br>
nilai x: 2<br>
nilai x: 3<br>
nilai x: 4<br>
nilai i: 0<br>
nilai i: 1<br>
nilai i: 2<br>
nilai i: 3<br>
nilai i: 4

### Function and Exception

```python
def test_function_return_value(input_value):
    return input_value * 2

print(test_function_return_value(4))
print("-----------------")

def my_function(temp_string):
    print(temp_string + "<---")
    return temp_string + "done"

print(my_function("Test 1"))
print(my_function("Test 2"))
print(my_function("Test 3"))
print("-----------------")

def your_function(temp_string):
    try:
        result = temp_string + 5
    except TypeError:
        print(temp_string + "<---")
    finally:
        print("yeaaay")

your_function("test 1")
your_function("test 2")
```
- output :<br>
8<br>
-----------------<br>
Test 1<---<br>
Test 1done<br>
Test 2<---<br>
Test 2done<br>
Test 3<---<br>
Test 3done<br>
-----------------<br>
test 1<---<br>
yeaaay<br>
test 2<---<br>
yeaaay

### Namespace

```python
global_var = 10
def test_namespace():
    private_var = 5
    global_var = 6

    print ("private_var :", private_var)
    print ("global_var :", global_var)

print("global_var:",global_var)
test_namespace()
```
- output :<br>
global_var: 10<br>
private_var : 5<br>
global_var : 6

### String Operator

```python
def test_string_operator():
    full_string = "this is full string"
    temp_string = "temp string"
    upper_string = "THIS IS UPPER"
    lower_string = "this is lower"

    # Concat :
    print(full_string+temp_string)
    # Slicing :
    print(full_string[3:6])
    # Lower :
    print(upper_string.lower())
    # Upper :
    print(lower_string.upper())
    # Len :
    print(len(full_string))
    # Strip :
    print(full_string.strip("t"))
    # Replace :
    print(full_string.replace("full","name"))
    # Split
    print(full_string.split("is"))

test_string_operator()
```
- output :<br>
this is full stringtemp string<br>
s i<br>
this is upper<br>
THIS IS LOWER<br>
19<br>
his is full string<br>
this is name string<br>
['th', ' ', ' full string']
