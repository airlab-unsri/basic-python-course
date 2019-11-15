students = ["akbar"]
students.append("muhammad")
print(students)

students.insert(1, "rizki")
print(students)

woman_students = ["baba", "bibi", "bubu", "bobo"]
students.extend(woman_students[0:2])
print(students)

students.sort()
print(students)

students.reverse()
print(students)

students.remove("muhammad")
print(students)
