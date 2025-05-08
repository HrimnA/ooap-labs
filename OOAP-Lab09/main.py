class Product:
    def __init__(self, state):
        self._state = state

    def set_state(self, state):
        print(f"[Originator] Зміна стану на: {state}")
        self._state = state

    def get_state(self):
        return self._state

    def save(self):
        print(f"[Originator] Збереження стану: {self._state}")
        return Memento(self._state)

    def restore(self, memento):
        self._state = memento.get_state()
        print(f"[Originator] Відновлення стану до: {self._state}")


class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class Caretaker:
    def __init__(self):
        self._history = []

    def save_state(self, memento):
        print(f"[Caretaker] Збережено стан: {memento.get_state()}")
        self._history.append(memento)

    def get_state(self, index):
        return self._history[index] if 0 <= index < len(self._history) else None

    def last_state(self):
        return self._history[-1] if self._history else None


def simulate_production_line():
    caretaker = Caretaker()
    product = Product("Початковий стан")

    product.set_state("Етап 1: обробка")
    caretaker.save_state(product.save())

    product.set_state("Етап 2: складання")
    caretaker.save_state(product.save())

    product.set_state("Етап 3: тестування")
    caretaker.save_state(product.save())

    print("\n[!] Виявлено збій. Повернення до попереднього стану...")
    product.restore(caretaker.get_state(1))

    product.set_state("Етап 3: повторне тестування")
    caretaker.save_state(product.save())


simulate_production_line()
