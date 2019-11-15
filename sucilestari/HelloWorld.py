"""
def my_function(temp_string):
    print(temp_string + "<--")
    return temp_string + "done"
 
print(my_function("Test1"))
print(my_function("Test2"))
print(my_function("Test3"))
"""

#conditional
def test_conditional():
    name = "suci"

    if(name == "suci"):
        print("this is if")
    elif(name == "tiara"):
        print("this is elif")
    else:
        print("this is else")



def test_looping():
    #looping for
    for x in range (0,5):
        print("nilai",x)

    #looping while
    i = 0
    while(i<5):
        print("nilai i : ",i)
        i+= 1
 
def my_function(input_value):
    return input_value * 2

global_var = 10
def test_namespace():
    private_var = 5
    global_var = 6

    print("private var = ",private_var)
    print("global var = ",global_var)

def test_string_operator():
    full_string = "this is full string"
    temp_string = "temp string"
    upper_string = "THIS IS UPPER"
    lower_string = "this is lower"
    
    print(full_string+temp_string)
    print(full_string[3:6])
    print(upper_string.lower())
    print(lower_string.upper())
    print(len(full_string))
    print(full_string.strip('t'))
    print(full_string.replace("full", "sum"))
    print(full_string.split("is"))
    print('hahahah')
    print("hahahah")

test_conditional()
test_looping()
print(my_function(5)) 
test_namespace()
print("global var = ",global_var)
test_string_operator()
