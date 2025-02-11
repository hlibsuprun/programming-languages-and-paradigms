class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def describeEmployee(self):
        return f"Pracownik: \t{self.name} Wiek: \t{self.age} Wynagrodzenie: \t{self.salary}"

    def updateSalary(self, newSalary):
        self.salary = newSalary