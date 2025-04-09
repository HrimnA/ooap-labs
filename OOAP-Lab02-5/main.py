from abc import ABC, abstractmethod

class Phone(ABC):
    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def get_delivery_time(self):
        pass

class USPhone(Phone):
    def get_price(self):
        return 780

    def get_delivery_time(self):
        return 5

class EastPhone(Phone):
    def get_price(self):
        return 520

    def get_delivery_time(self):
        return 17

class PhoneFactory(ABC):
    @abstractmethod
    def create_phone(self):
        pass

class USPhoneFactory(PhoneFactory):
    def create_phone(self):
        return USPhone()

class EastPhoneFactory(PhoneFactory):
    def create_phone(self):
        return EastPhone()

class PhoneStore:
    def __init__(self, factory: PhoneFactory):
        self.factory = factory

    def order_phone(self):
        phone = self.factory.create_phone()
        price = phone.get_price()
        delivery_time = phone.get_delivery_time()
        return price, delivery_time

def main():
    print("Select the country of manufacture:")
    print("1. USA")
    print("2. Eastern country")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        factory = USPhoneFactory()
    elif choice == "2":
        factory = EastPhoneFactory()
    else:
        print("Invalid choice!")
        print()
        return

    store = PhoneStore(factory)
    price, delivery_time = store.order_phone()

    print(f"The price of the phone is: ${price}")
    print(f"Delivery time is: {delivery_time} days")
    print()

if __name__ == "__main__":
    print("Welcome to the phone store!")
    while True: main()