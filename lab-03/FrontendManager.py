from EmployeesManager import EmployeesManager
from Employee import Employee

class FrontendManager:
    def __init__(self):
        self.manager = EmployeesManager()

    def login(self):
        print("Logowanie do systemu")
        username = input("Podaj nazwę użytkownika: ")
        password = input("Podaj hasło: ")
        if username == "admin" and password == "admin":
            print("Logowanie udane")
            return True
        print("Niepoprawne dane logowania.")
        return False

    def displayMenu(self):
        print("\nSystem zarządzania pracownikami")
        print("1. Dodaj nowego pracownika")
        print("2. Wyświetl wszystkich pracowników")
        print("3. Usuń pracowników w przedziale wiekowym")
        print("4. Znajdź pracownika po nazwisku")
        print("5. Zaktualizuj wynagrodzenie pracownika")
        print("6. Zakończ")

    def getEmployeeDetails(self):
        while True:
            try:
                name = input("Wprowadź imię i nazwisko pracownika: ")
                if not name.strip():
                    raise ValueError("Imię i nazwisko nie mogą być puste")
                age = int(input("Wprowadź wiek pracownika: "))
                if age <= 0:
                    raise ValueError("Wiek musi być większy od 0")
                salary = int(input("Wprowadź wynagrodzenie pracownika: "))
                if salary < 0:
                    raise ValueError("Wynagrodzenie nie może być ujemne")
                return Employee(name, age, salary)
            except ValueError as e:
                print(f"Błąd: {e}. Spróbuj ponownie")

    def start(self):
        if not self.login():
            return

        while True:
            self.displayMenu()
            choice = input("Wybierz opcję: ")

            if choice == '1':
                employee = self.getEmployeeDetails()
                self.manager.addEmployee(employee)
            elif choice == '2':
                self.manager.displayAllEmployees()
            elif choice == '3':
                try:
                    minAge = int(input("Podaj minimalny wiek: "))
                    maxAge = int(input("Podaj maksymalny wiek: "))
                    self.manager.removeEmployeesInAgeRange(minAge, maxAge)
                except ValueError:
                    print("Wiek musi być liczbą")
            elif choice == '4':
                name = input("Podaj imię i nazwisko pracownika do wyszukania: ")
                self.manager.findEmployeeByName(name)
            elif choice == '5':
                name = input("Podaj imię i nazwisko pracownika, którego wynagrodzenie chcesz zaktualizować: ")
                try:
                    newSalary = int(input("Podaj nowe wynagrodzenie: "))
                    self.manager.updateEmployeeSalary(name, newSalary)
                except ValueError:
                    print("Wynagrodzenie musi być liczbą")
            elif choice == '6':
                print("Zakończenie systemu")
                break
            else:
                print("Niepoprawna opcja, spróbuj ponownie")
