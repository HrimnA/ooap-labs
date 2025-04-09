from abc import ABC, abstractmethod


class SoldierComponent(ABC):
    @abstractmethod
    def execute_order(self, order: str):
        pass


class Soldier(SoldierComponent):
    name = "name"
    def __init__(self, name: str):
        self.name = name

    def execute_order(self, order: str):
        print(f"Солдат {self.name} виконує наказ: {order}")


class Squad(SoldierComponent):
    def __init__(self, name: str):
        self.name = name
        self.members = []

    def add(self, soldier: SoldierComponent):
        self.members.append(soldier)

    def remove(self, soldier: SoldierComponent):
        self.members.remove(soldier)

    def execute_order(self, order: str):
        print(f"{self.name} отримує наказ: {order}")
        for member in self.members:
            member.execute_order(order)


soldier1 = Soldier("Солдат А")
soldier2 = Soldier("Солдат Б")
soldier3 = Soldier("Солдат В")

squad = Squad("1-й взвод")
squad.add(soldier1)
squad.add(soldier2)

company = Squad("2-й взвод")
company.add(squad)
company.add(soldier3)

print("--- Наказ одному солдату ---")
soldier1.execute_order("Кроком руш!")

print("\n--- Наказ взводу ---")
squad.execute_order("Стій!")

print("\n--- Наказ роті ---")
company.execute_order("Направо!")