students = ["Sendy"]
students.append("Ramadhan")
print(students)

students.insert(1, "D")
print(students)

woman_students = ["Runu", "Rana", "Rini", "Rono"]
students.extend(woman_students[0:4])
print(students)

students.sort()
print(students)

students.reverse()
print(students)

students.remove("Ramadhan")
print(students)