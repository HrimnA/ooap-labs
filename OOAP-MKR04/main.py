from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, new_bid, bidder_name):
        pass

class AuctionParticipant(Observer):
    def __init__(self, name, card_number):
        self.name = name
        self.card_number = card_number

    def update(self, new_bid, bidder_name):
        if self.name != bidder_name:
            print(f"{self.name} бачить, що {bidder_name} запропонував нову ставку: {new_bid} грн.")

    def make_bid(self, auctioneer, amount):
        print(f"{self.name} піднімає картку {self.card_number} і пропонує ставку {amount} грн.")
        auctioneer.receive_bid(amount, self)

class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass

class Auctioneer(Subject):
    def __init__(self):
        self._observers = []
        self.current_bid = 0
        self.current_bidder = None

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self.current_bid, self.current_bidder.name)

    def receive_bid(self, amount, bidder):
        if amount > self.current_bid:
            self.current_bid = amount
            self.current_bidder = bidder
            print(f"Ведучий приймає нову ставку: {amount} грн від {bidder.name}")
            self.notify()
        else:
            print(f"Ставка {amount} грн від {bidder.name} є нижчою або рівною поточній ставці. Відхилено.")

if __name__ == "__main__":
    auctioneer = Auctioneer()

    participant1 = AuctionParticipant("Учасник А", 1)
    participant2 = AuctionParticipant("Учасник Б", 2)
    participant3 = AuctionParticipant("Учасник В", 3)

    auctioneer.attach(participant1)
    auctioneer.attach(participant2)
    auctioneer.attach(participant3)

    participant1.make_bid(auctioneer, 100)
    participant2.make_bid(auctioneer, 150)
    participant3.make_bid(auctioneer, 120)
    participant3.make_bid(auctioneer, 200)
