def test_conditional():
    name = "Sendy"
    
    if(name == "Sendy"):
        print("this is if")
    elif(name == "Domu"):
        print("this is elif")
    else:
        print("this is else")
        
def test_looping():
    for x in range(0,5):
        print("nilai x",x)
    
    i = 0
    while(i<5):
        print("nilai i", i)

#print(test_looping())   

global_var = 10
def test_namespace():
    private_var = 15
    print("private var = ",private_var)
    print("global var = ",global_var)

print(test_namespace())

def test_string_operator():
    full_string = "this is full string"
    temp_string = "temp string"
    upper_string = "this is upper"
    lower_string = "this is lower"
    
    print(full_string+temp_string)
    print(full_string[3:6])
    print(upper_string.lower())
    print(lower_string.upper())
    print(len(full_string))
    print(full_string.strip('t'))
    print(full_string.replace("full","some"))
    print(full_string.split(" "))
    
test_string_operator()

def test_function(value):
    return value;

print(test_function(4))