from functools import wraps


def bonus_decorator(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        base_salary = func(self, *args, **kwargs)
        return base_salary + self.bonus

    return wrapper


class Employee:
    def __init__(self, name, qualification, base_salary):
        self.name = name
        self.qualification = qualification
        self.base_salary = base_salary
        self.bonus = 0
        self.overtime_hours = 0

    def add_overtime(self, hours):
        self.overtime_hours += hours

    def set_bonus(self, amount):
        self.bonus = amount

    @bonus_decorator
    def calculate_salary(self):
        return self.base_salary

    def __repr__(self):
        return f"{self.name} ({self.qualification}): {self.calculate_salary()} USD"


class FullTimeEmployee(Employee):
    def __init__(self, name, qualification):
        super().__init__(name, qualification, 4000)


class Contractor(Employee):
    def __init__(self, name, qualification):
        super().__init__(name, qualification, 30)

    @bonus_decorator
    def calculate_salary(self):
        return self.base_salary * 160


class PayrollSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def update_qualification(self, employee, new_qualification):
        employee.qualification = new_qualification

    def calculate_salaries(self):
        return {emp.name: emp.calculate_salary() for emp in self.employees}

    def top_10_overtime(self):
        top_employees = sorted(self.employees, key=lambda x: x.overtime_hours, reverse=True)[:10]
        for emp in top_employees:
            emp.set_bonus(emp.calculate_salary())  # Премія у розмірі окладу
        return top_employees


if __name__ == "__main__":
    payroll = PayrollSystem()
    employees = [
        FullTimeEmployee("Alice", "Senior"),
        Contractor("Bob", "Junior"),
        FullTimeEmployee("Charlie", "Middle"),
        Contractor("David", "Trainee"),
        FullTimeEmployee("Eve", "Senior"),
        Contractor("Frank", "Middle"),
        FullTimeEmployee("Grace", "Junior"),
        Contractor("Hank", "Senior"),
        FullTimeEmployee("Ivy", "Trainee"),
        Contractor("Jack", "Middle"),
        FullTimeEmployee("Karen", "Junior"),
        Contractor("Leo", "Senior"),
        FullTimeEmployee("Mia", "Middle"),
        Contractor("Nathan", "Trainee"),
        FullTimeEmployee("Olivia", "Senior"),
        Contractor("Paul", "Middle"),
        FullTimeEmployee("Quinn", "Junior"),
        Contractor("Rachel", "Senior")
    ]

    for emp in employees:
        payroll.add_employee(emp)

    overtime_hours = [20, 30, 25, 15, 35, 10, 5, 40, 22, 18, 14, 50, 27, 33, 28, 45, 12, 38]
    for emp, hours in zip(employees, overtime_hours):
        emp.add_overtime(hours)

    print("Список зарплат:", payroll.calculate_salaries())
    print("Топ-10 за понаднормові години:", payroll.top_10_overtime())
