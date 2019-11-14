numbers = [10,20,30]
#list comprehensions
multiply10 = [number * 10 for number in numbers]
print(multiply10)

# the usual way
result = []
for number in numbers:
    result.append(number * 10)
print(result)    