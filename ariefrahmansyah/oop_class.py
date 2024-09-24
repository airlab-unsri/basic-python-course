class Employee:
    'Common base class for all employees'

    # empCount is class attribute, defined outside the constructor
    empCount = 0

    def __init__(self, name, salary):
        # name and salary are instance attributes, defined inside the constructor.
        self.name = name
        self.salary = salary

        Employee.empCount += 1

    # displayCount is method.
    def displayCount(self):
        print("Total employee:", Employee.empCount)

    # displayEmployee is method.
    def displayEmployee(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
emp1.displayEmployee()
