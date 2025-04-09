class Car:
    def __init__(self):
        self.engine_type = None
        self.engine_volume = None
        self.abs = None
        self.esp = None
        self.airbags = None
        self.onboard_computer = None
        self.ac_system = None
        self.interior = None
        self.price = None

    def __str__(self):
        return (f"Двигун: {self.engine_type}, Об'єм: {self.engine_volume} л\n"
                f"ABS: {'Так' if self.abs else 'Ні'}, ESP: {'Так' if self.esp else 'Ні'}\n"
                f"Подушки безпеки: {self.airbags}\n"
                f"Бортовий комп'ютер: {'Так' if self.onboard_computer else 'Ні'}\n"
                f"Кліматична система: {self.ac_system}\n"
                f"Обшивка салону: {self.interior}\n"
                f"Ціна: {self.price} грн")

class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_engine_type(self):
        raise NotImplementedError

    def set_engine_volume(self):
        raise NotImplementedError

    def set_abs(self):
        raise NotImplementedError

    def set_esp(self):
        raise NotImplementedError

    def set_airbags(self):
        raise NotImplementedError

    def set_onboard_computer(self):
        raise NotImplementedError

    def set_ac_system(self):
        raise NotImplementedError

    def set_interior(self):
        raise NotImplementedError

    def set_price(self):
        raise NotImplementedError

    def get_car(self):
        return self.car

class BasicCarBuilder(CarBuilder):
    def set_engine_type(self):
        self.car.engine_type = "Бензиновий"

    def set_engine_volume(self):
        self.car.engine_volume = 1.6

    def set_abs(self):
        self.car.abs = True

    def set_esp(self):
        self.car.esp = False

    def set_airbags(self):
        self.car.airbags = 2

    def set_onboard_computer(self):
        self.car.onboard_computer = False

    def set_ac_system(self):
        self.car.ac_system = "Кондиціонер"

    def set_interior(self):
        self.car.interior = "Тканина"

    def set_price(self):
        self.car.price = 300000


class ComfortCarBuilder(CarBuilder):
    def set_engine_type(self):
        self.car.engine_type = "Дизельний"

    def set_engine_volume(self):
        self.car.engine_volume = 2.0

    def set_abs(self):
        self.car.abs = True

    def set_esp(self):
        self.car.esp = True

    def set_airbags(self):
        self.car.airbags = 6

    def set_onboard_computer(self):
        self.car.onboard_computer = True

    def set_ac_system(self):
        self.car.ac_system = "Клімат-контроль"

    def set_interior(self):
        self.car.interior = "Шкіра"

    def set_price(self):
        self.car.price = 500000

# Будівельник для преміумної комплектації
class PremiumCarBuilder(CarBuilder):
    def set_engine_type(self):
        self.car.engine_type = "Гібридний"

    def set_engine_volume(self):
        self.car.engine_volume = 2.5

    def set_abs(self):
        self.car.abs = True

    def set_esp(self):
        self.car.esp = True

    def set_airbags(self):
        self.car.airbags = 8

    def set_onboard_computer(self):
        self.car.onboard_computer = True

    def set_ac_system(self):
        self.car.ac_system = "Клімат-контроль 2-зонний"

    def set_interior(self):
        self.car.interior = "Шкіра преміум"

    def set_price(self):
        self.car.price = 700000

class SportCarBuilder(CarBuilder):
    def set_engine_type(self):
        self.car.engine_type = "Бензиновий"

    def set_engine_volume(self):
        self.car.engine_volume = 3.0

    def set_abs(self):
        self.car.abs = True

    def set_esp(self):
        self.car.esp = True

    def set_airbags(self):
        self.car.airbags = 4

    def set_onboard_computer(self):
        self.car.onboard_computer = True

    def set_ac_system(self):
        self.car.ac_system = "Клімат-контроль"

    def set_interior(self):
        self.car.interior = "Алькантара"

    def set_price(self):
        self.car.price = 900000

class CarDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_car(self):
        self.builder.set_engine_type()
        self.builder.set_engine_volume()
        self.builder.set_abs()
        self.builder.set_esp()
        self.builder.set_airbags()
        self.builder.set_onboard_computer()
        self.builder.set_ac_system()
        self.builder.set_interior()
        self.builder.set_price()
        return self.builder.get_car()

# Використання програми
if __name__ == "__main__":
    while True:
        print("Оберіть комплектацію:\n1 - Basic\n2 - Comfort\n3 - Premium\n4 - Sport")
        choice = input("Ваш вибір: ")

        if choice == "1":
            builder = BasicCarBuilder()
        elif choice == "2":
            builder = ComfortCarBuilder()
        elif choice == "3":
            builder = PremiumCarBuilder()
        elif choice == "4":
            builder = SportCarBuilder()
        else:
            print("Невірний вибір!")
            print()
            continue

        director = CarDirector(builder)
        car = director.build_car()
        print("\nХарактеристики обраної комплектації:")
        print(car)
        print()