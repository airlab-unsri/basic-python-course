students = ["Abi"]
students.append("Yogi")
print(students)
print("------------------------")

students.insert(0, "Imam")
print(students)
print("------------------------")

womenStudents = ["Tiara", "suci", "Rini"]
students.extend(womenStudents[0:2])
print(students)
print("------------------------")

students.sort()
print(students)
print("------------------------")

students.reverse()
print(students)
print("------------------------")

students.remove("Abi")
print(students)
