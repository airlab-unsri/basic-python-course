class Employe:
    empCount=0    

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employe.empCount +=1

    def displayCount(self):
        print("total Employe %d" % Employe.empCount)

    def displayEmploye(self):
        print("name : ", self.name, ", salary : ", self.salary) 

emp = Employe("NANI", 200)
emp.displayCount()
Employe.empCount               