import json
from dataclasses import dataclass


@dataclass
class Employee:
    name: str
    last_name: str
    b_year: int
    salary: float

    def to_dict(self):
        return self.__dict__


try:
    with open("employees.json") as f:
        employees = json.load(f)
except FileNotFoundError:
    employees = []


while True:
    command = input("Co chcesz zrobic? [d - dodaj, w - wypisz, k-koniec]")
    if command == "d":
        name = input("Imie:")
        last_name = input("Nazwisko:")
        b_year = int(input("Rok urodzenia:"))
        salary = float(input("Pensja:"))
        employee = Employee(name, last_name, b_year, salary)
        employees.append(employee)

        print(employees)
        print([e.to_dict() for e in employees])

    elif command == "w":
        for e in employees:
            print(e)

    elif command == "k":
        with open("employees.json", "w", encoding="CP1250") as f:
            json.dump([e.to_dict() for e in employees], f)
        exit()
