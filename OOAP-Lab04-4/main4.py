from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def calculate_salary(self, *args):
        pass

class HourlyPayment(PaymentMethod):
    def __init__(self, hourly_rate):
        self.hourly_rate = hourly_rate

    def calculate_salary(self, hours_worked):
        return self.hourly_rate * hours_worked

class PieceworkPayment(PaymentMethod):
    def __init__(self, rate_per_unit):
        self.rate_per_unit = rate_per_unit

    def calculate_salary(self, units_produced):
        return self.rate_per_unit * units_produced

class Employee(ABC):
    def __init__(self, name, position, payment_method: PaymentMethod):
        self.name = name
        self.position = position
        self.payment_method = payment_method

    @abstractmethod
    def get_salary(self):
        pass

    def display_info(self):
        print(f"Ім'я: {self.name}, Посада: {self.position}")
        print(f"Заробітна плата: {self.get_salary()} грн\n")

class HourlyEmployee(Employee):
    def __init__(self, name, position, payment_method: PaymentMethod, hours_worked):
        super().__init__(name, position, payment_method)
        self.hours_worked = hours_worked

    def get_salary(self):
        return self.payment_method.calculate_salary(self.hours_worked)

class PieceworkEmployee(Employee):
    def __init__(self, name, position, payment_method: PaymentMethod, units_produced):
        super().__init__(name, position, payment_method)
        self.units_produced = units_produced

    def get_salary(self):
        return self.payment_method.calculate_salary(self.units_produced)

if __name__ == "__main__":
    hourly_payment = HourlyPayment(hourly_rate=100)  # 100 грн за годину
    piecework_payment = PieceworkPayment(rate_per_unit=50)  # 50 грн за одиницю

    employee1 = HourlyEmployee(name="Іван Іваненко", position="Електрик", payment_method=hourly_payment, hours_worked=160)
    employee2 = PieceworkEmployee(name="Петро Петренко", position="Монтажник", payment_method=piecework_payment, units_produced=30)

    employee1.display_info()
    employee2.display_info()
