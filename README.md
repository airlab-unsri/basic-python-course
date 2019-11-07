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
### IF Statement
```python
def testConditional():
    name = 'Darmawan'

    if (name == "Darmawan"):
        print("ini abi")
    elif (name == "imam"):
        print("ini elif")
    else:
        print("else")

testConditional()
```
### FOR Looping
```python
def testLooping():
    for x in range (0,5):
        print("nilai x : ", x)
        
testLooping()
```
### Function with Parameter
```python
def myFunc(inputValue):
    return inputValue * 4
print(myFunc(3))
```

### Global variable
```python
globalVar = 10
def testNameSpace():
    privateVar = 6
    globalVar = 7

    print("Private Variable : ", privateVar)
    print("Global Variable : ", globalVar)

testNameSpace()
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
