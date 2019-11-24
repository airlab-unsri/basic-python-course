class SomeClass:
    def __init__(self):
        self.__instance_variable = 'this is a private instance variable'

    def __private_method(self):
        print('this is printed by private method')

an_instance = SomeClass()

# accessing instance private variable
try:
    print(an_instance.__instance_variable)
    print('bisa mengakses private instance variable')
except AttributeError as error_message:
    print('tidak bisa mengakses private instance attribute:\n\t' + str(error_message))

# assigning instance private variable
an_instance.__instance_variable = 'private variable re-assigned'

# accessing instance private variable once again
print(an_instance.__instance_variable)
