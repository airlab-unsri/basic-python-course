def testConditional():
    name = 'Darmawan'

    if (name == "Darmawan"):
        print("ini abi")
    elif (name == "imam"):
        print("ini elif")
    else:
        print("else")

testConditional()

print("-------------------------")
def testLooping():
    for x in range(0,5):
        print("nilai x : ", x)

testLooping()

print("-------------------------")
def myFunc(inputValue):
    return inputValue * 4
print(myFunc(3))

print("-------------------------")
globalVar = 10
def testNameSpace():
    privateVar = 6
    globalVar = 7

    print("Private Variable : ", privateVar)
    print("Global Variable : ", globalVar)

testNameSpace()
print("Global Variable 2 : ", globalVar)

print("-------------------------")
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

print("------------------------------")
def whileLoop():
    i = 1
    while i < 6:
        print(i)
        i+=1

whileLoop()

print("------------------------------")
input("Enter Your Name : ")
