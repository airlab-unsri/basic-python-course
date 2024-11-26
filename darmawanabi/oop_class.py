class Employee:

    # mendefinisikan atribut diluar konstruktor
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        # name dan salary merupakan atribut yang didefinisikan didalan cons

        Employee.empCount += 1

    def displayCount(self):
        print("Total Karyawan : ", Employee.empCount)
        
    def displayEmployee(self):
        print("Nama : ", self.name)
        print("Gaji : ", self.salary)

emp1 = Employee("Darmawan Abinugroho", 1000)
emp1.displayEmployee()
emp1.displayCount()
