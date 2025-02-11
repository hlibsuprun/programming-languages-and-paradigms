import json
from Employee import Employee

class EmployeesManager:
    def __init__(self, filename="employees.json"):
        self.filename = filename
        self.employees = self.loadFromFile()

    def saveToFile(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            data = [
                {"name": emp.name, "age": emp.age, "salary": emp.salary} for emp in self.employees
            ]
            json.dump(data, file, indent=4)

    def loadFromFile(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return [Employee(emp['name'], emp['age'], emp['salary']) for emp in data]
        except FileNotFoundError:
            return []

    def addEmployee(self, employee):
        self.employees.append(employee)
        self.saveToFile()

    def displayAllEmployees(self):
        if not self.employees:
            print("Brak pracowników.")
        for employee in self.employees:
            print(employee.describeEmployee())

    def removeEmployeesInAgeRange(self, minAge, maxAge):
        self.employees = [emp for emp in self.employees if not (minAge <= emp.age <= maxAge)]
        self.saveToFile()
        print(f"Pracownicy w przedziale wiekowym {minAge}-{maxAge} zostali usunięci.")

    def findEmployeeByName(self, name):
        foundEmployee = [emp for emp in self.employees if emp.name.lower() == name.lower()]
        if foundEmployee:
            for employee in foundEmployee:
                print(employee.describeEmployee())
        else:
            print(f"Nie znaleziono pracownika o nazwisku {name}.")

    def updateEmployeeSalary(self, name, newSalary):
        for employee in self.employees:
            if employee.name.lower() == name.lower():
                employee.updateSalary(newSalary)
                self.saveToFile()
                print(f"Wynagrodzenie pracownika {name} zostało zaktualizowane.")
                return
        print(f"Pracownik o nazwisku {name} nie został znaleziony.")
