from abc import ABC, abstractmethod

class AddressInterface(ABC):
    @abstractmethod
    def set_address(self, street, city, zipcode):
        pass

    @abstractmethod
    def get_address(self):
        pass

class Address(AddressInterface):
    def __init__(self, street='', city='', zipcode=''):
        self._street = street
        self._city = city
        self._zipcode = zipcode

    def set_address(self, street, city, zipcode):
        self._street = street
        self._city = city
        self._zipcode = zipcode

    def get_address(self):
        return f'{self._street}, {self._city}, {self._zipcode}'

class Person:
    def __init__(self, name, address_delegate):
        self._name = name
        self._address_delegate = address_delegate

    def set_address(self, street, city, zipcode):
        self._address_delegate.set_address(street, city, zipcode)

    def get_address(self):
        return self._address_delegate.get_address()

    def get_person_info(self):
        return f'Name: {self._name}, Address: {self.get_address()}'

    def set_name(self, name):
        self._name = name

class AddressBook:
    def __init__(self):
        self._entries = []

    def add_person(self, person):
        self._entries.append(person)

    def edit_person(self, index, name=None, street=None, city=None, zipcode=None):
        if 0 <= index < len(self._entries):
            person = self._entries[index]
            if name:
                person.set_name(name)
            if street and city and zipcode:
                person.set_address(street, city, zipcode)
        else:
            print(f"Person with index {index} not found!")

    def delete_person(self, index):
        if 0 <= index < len(self._entries):
            self._entries.pop(index)
        else:
            print(f"Person with index {index} not found!")

    def show_all_entries(self):
        if not self._entries:
            print("Address book is empty.")
        for index, person in enumerate(self._entries):
            print(f"{index}: {person.get_person_info()}")

    def auto_fill(self):
        sample_data = [
            ("Ivan Koval", Address("Shevchenko St", "Kyiv", "01001")),
            ("Petro Leshuk", Address("Khmelnytskyy St", "Lviv", "79000")),
            ("Olena Shevchenko", Address("Franko St", "Odessa", "65000")),
            ("Mykola Symonenko", Address("Gogol St", "Kharkiv", "61000")),
            ("Dmytro Hrytsenko", Address("Grushevskyy St", "Dnipro", "49000"))
        ]
        for name, address in sample_data:
            person = Person(name, address)
            self.add_person(person)

def create_person():
    try:
        name = input("Enter person's name: ")
        street = input("Enter street: ")
        city = input("Enter city: ")
        zipcode = input("Enter zipcode: ")

        if not name or not street or not city or not zipcode:
            raise ValueError("All fields must be filled.")

        address = Address(street, city, zipcode)
        return Person(name, address)
    except ValueError as ve:
        print(f"Error: {ve}")
        return None

def get_valid_index(prompt, max_index):
    try:
        index = int(input(prompt))
        if index < 0 or index >= max_index:
            raise IndexError("Index out of range.")
        return index
    except ValueError:
        print("Error: Please enter a valid integer.")
        return None
    except IndexError as ie:
        print(f"Error: {ie}")
        return None

def menu():
    address_book = AddressBook()

    while True:
        print("\nAddress Book Menu:")
        print("1. Add a person")
        print("2. Edit a person")
        print("3. Delete a person")
        print("4. Show all entries")
        print("5. Auto-fill address book with sample data")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            person = create_person()
            if person:
                address_book.add_person(person)
                print("Person added successfully.")
        elif choice == '2':
            address_book.show_all_entries()
            if len(address_book._entries) == 0:
                continue
            index = get_valid_index("Enter the index of the person to edit: ", len(address_book._entries))
            if index is not None:
                name = input("Enter new name (leave empty to keep current): ")
                street = input("Enter new street (leave empty to keep current): ")
                city = input("Enter new city (leave empty to keep current): ")
                zipcode = input("Enter new zipcode (leave empty to keep current): ")

                if street and city and zipcode:
                    address_book.edit_person(index, name, street, city, zipcode)
                else:
                    address_book.edit_person(index, name)

                print("Person edited successfully.")
        elif choice == '3':
            address_book.show_all_entries()
            if len(address_book._entries) == 0:
                continue
            index = get_valid_index("Enter the index of the person to delete: ", len(address_book._entries))
            if index is not None:
                address_book.delete_person(index)
                print("Person deleted successfully.")
        elif choice == '4':
            address_book.show_all_entries()
        elif choice == '5':
            address_book.auto_fill()
            print("Address book has been auto-filled with sample data.")
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    menu()
