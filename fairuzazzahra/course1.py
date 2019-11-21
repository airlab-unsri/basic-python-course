# conditional if
def test_conditional():
    name = "zahra"

    if (name == "zahra"):
        print("this is if")
    elif (name == "fairuz"):
        print("this is  elif")
    else:
        print("this is else")
test_conditional()
print("===============")

# looping
def test_looping():
    for x in  range(0,5):
        print("nilai x", x)

    i = 0
    while (i < 5):
        print("nilai i : ", i)
        i += 1
test_looping()
print("===============")

# function
def test_function_return_value(input_value):
    return input_value + 2
print(test_function_return_value(5))
print("===============")

# private and global variable
global_var = 10
def test_namespace():
    private_var = 5
    global_var = 6

    print("private val : ", private_var)
    print("global val : ", global_var)

test_namespace()
print("global val : ", global_var)
print("===============")

# string operator
def test_string_operator():
    full_string = "this is full string"
    temp_string = "temp string"
    upper_string = "THIS IS UPPER"
    lower_string = "this is lower"

    print(full_string + temp_string)
    # slicing
    print(full_string[3:6])
    # upper to lower
    print(upper_string.lower())
    # lower to upper
    print(lower_string.upper())
    # total length
    print(len(full_string))
    # letter strip
    print(full_string.strip('t'))
    # replace word
    print(full_string.replace("full", "some"))
    # letter split
    print(full_string.split('s'))
test_string_operator()
