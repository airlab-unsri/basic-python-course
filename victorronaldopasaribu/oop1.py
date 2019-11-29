class Employee:
   'Common base class for all employees'
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

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
#emp1.Employee()
emp1.displayEmployee()
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)

