class Employee:
   empCount = 0

   def Employee(self):
      print("Total Employee %d" % Employee.empCount)

   def __init__(self, name, salary):
      print("constructor created")
      self.name = name
      self.salary = salary
      Employee.empCount += 1

   def displayCount(self):
     print("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print("Name : ", self.name,  ", Salary: ", self.salary)

emp1 = Employee("kiki", 2000)
#emp1.Employee()
emp1.displayEmployee()
emp2 = Employee("riri", 5000)