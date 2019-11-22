a_tuple = ('apple', 'orange')  # pack a tuple

print(a_tuple)
print(len(a_tuple))
print(a_tuple[1])

try:
    a_tuple[1] = 'mango'  # throws error because tuples are immutable
except TypeError as error_message:
    print('error bro!', str(error_message))

a_tuple = ('mango', 'avocado')  # we still can reassign the variable though
print(a_tuple)

(fruit_1, fruit_2) = a_tuple  # unpack a tuple values into variables
print(fruit_1)
print(fruit_2)

(buah_1, buah_2) = ('mangga', 'apel')  # pack & unpack at the same time
print(buah_1)
print(buah_2)
