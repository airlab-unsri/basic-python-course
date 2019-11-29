def my_function(temp_string):
    try:
        result = temp_string + 5
    except TypeError:
        print(temp_string + " is not a string")
    finally:
        print('finally\n')


my_function(3)
my_function('test1')
my_function('test2')
my_function('test3')
