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
