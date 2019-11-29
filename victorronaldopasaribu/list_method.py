students = ["faisal"]
students.append("roni")
print(students)

students.insert(1, "arief")
print(students)

women_students = ["wenty","kekek","rini","melinia"]
#students.extend(women_students)
students.extend(women_students[0:1])
print(students)

students.sort()
print(students)

students.reverse()
print(students)

students.remove("faisal")
print(students)