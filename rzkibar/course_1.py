def test_condition():
    name = "rizki"
    
    if(name=="rizki"):
        print("this is if")
    elif(name=="rizka"):    
        print("this is elif")
    else:
        print("this is else")
 
def test_looping():
    for x in range (0,5):
        print("nilai x: ",x)
    
    i = 0
    while (i<5):
        print("nilai i: ",i)
        i+=1
        
def test_function_return_value(input_value):
    return input_value * 2

global_var = 10
def test_namespace():
    private_var = 5
    global_var = 6

    print("private val: ", private_var)
    print("private val: ", global_var)
    
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
