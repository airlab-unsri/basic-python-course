print("Hello World")

def test_conditional():
    name = "victor"
    
    if(name == "victor"):
        print("this is if")
    elif (name == "ronaldo"):   
        print("this is elif")
    else:
        print("this is else")
        
def test_looping():
    for x in range(0,5):
        print("nilai x",x)
        
    i=0
    while(i<5):
        print("nilai i: ",i)
        i += 1
        
def test_function_return_value(input_value):
    return input_value * 2


global_var = 10
def test_namespace():
    private_val = 5
    global_var = 6
    
    print("private val:",private_val)
    print("global var:",global_var)
    
test_conditional()
test_looping()
print(test_function_return_value(5))
    
def test_string_operator():
    full_string = "this is full string"
    temp_string = "temp string"
    upper_string = "THIS IS UPPER"
    lower_string = "this is lower"
    
    print(full_string+temp_string)
    print(full_string[3:6])
    print(upper_string.lower())
    print(lower_string.upper())
    print(full_string.strip('t'))
    print(full_string.replace("full","some"))
    print(full_string.split(" "))
    
test_string_operator()
    
def test_list():
    mylist = ['Python_list','Java','10','20']
    print(mylist)
    print(mylist[0])
    mylist[1]='spark'
    print(mylist)
    print(len(mylist))
    mylist.append(30)
    print(mylist)
    
test_list()
    
def string_formatting():
    name = "John"
    print("Hello, %s!" %name)
    age = 23
    print("%s is %d years old."% (name, age))
    mylist = [1,2,3]
    print("A list : %s" % mylist)
    
string_formatting()

def boolean_operators():
    isSunday = True
    isHoliday = True
    if isHoliday and isSunday:
        print('Sunday is a Funday!!')
    else:
        print('Not holiday bro!! Please start working :(')
    isSunday = False
    isHoliday = True
    if isHoliday and isSunday:
        print('Sunday is a Funday!!')
    else:
        print('Not holiday bro!! Please start working :(')
    isSunday = True
    isHoliday = False
    if isHoliday or isSunday:
        print('Sunday is a Funday!!')
    else:
        print('Not holiday bro!! Please start working :(')
    isSunday = True
    isHoliday = False
    if not isHoliday:
        print('Please start working, it is not holiday!!')
    else:
        print('Today is holiday!!')
        
boolean_operators()
