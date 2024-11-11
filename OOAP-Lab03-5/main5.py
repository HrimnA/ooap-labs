import copy
from abc import ABC, abstractmethod
from datetime import date

class Resident:
    def __init__(self, name, birth_date, faculty, group, education_form):
        self.name = name
        self.birth_date = birth_date
        self.faculty = faculty
        self.group = group
        self.education_form = education_form

    def __str__(self):
        return (f"ПІБ: {self.name}, Дата народження: {self.birth_date}, "
                f"Факультет: {self.faculty}, Група: {self.group}, "
                f"Форма навчання: {self.education_form}")

    def calculate_rent(self):
        return 500 if self.education_form == "держзамовлення" else 1000

class Room(ABC):
    def __init__(self, room_type, max_residents):
        self.room_type = room_type
        self.max_residents = max_residents
        self.residents = []

    def add_resident(self, resident):
        if len(self.residents) < self.max_residents:
            self.residents.append(resident)
        else:
            raise Exception("У кімнаті немає місць!")

    @abstractmethod
    def clone(self):
        pass

    def __str__(self):
        room_info = (f"Тип кімнати: {self.room_type}, Кількість місць: {self.max_residents}, "
                     f"Кількість мешканців: {len(self.residents)}\n")
        for resident in self.residents:
            room_info += f"{resident}\nКвартплата: {resident.calculate_rent()} грн\n"
        return room_info

class DoubleRoom(Room):
    def __init__(self):
        super().__init__("Двомісна кімната", 2)

    def clone(self):
        return copy.deepcopy(self)

class TripleRoom(Room):
    def __init__(self):
        super().__init__("Тримісна кімната", 3)

    def clone(self):
        return copy.deepcopy(self)

class DormitoryManager:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def generate_report(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            for room in self.rooms:
                file.write(str(room))
                file.write("\n" + "-"*40 + "\n")

if __name__ == "__main__":
    double_room_prototype = DoubleRoom()
    triple_room_prototype = TripleRoom()

    room1 = double_room_prototype.clone()
    room2 = triple_room_prototype.clone()

    room1.add_resident(Resident("Іваненко Іван Іванович", date(2000, 5, 15), "Фізичний", "ФІ-1", "держзамовлення"))
    room1.add_resident(Resident("Петренко Петро Петрович", date(2001, 3, 10), "Фізичний", "ФІ-1", "контракт"))

    room2.add_resident(Resident("Сидоренко Сидір Сидорович", date(2000, 9, 25), "Хімічний", "ХМ-2", "держзамовлення"))
    room2.add_resident(Resident("Мельник Микола Миколайович", date(2001, 11, 5), "Хімічний", "ХМ-2", "контракт"))
    room2.add_resident(Resident("Коваль Костянтин Костянтинович", date(1999, 7, 20), "Хімічний", "ХМ-2", "контракт"))

    manager = DormitoryManager()
    manager.add_room(room1)
    manager.add_room(room2)
    manager.generate_report("dormitory_report.txt")

    print("Звіт сформовано у файлі dormitory_report.txt")
