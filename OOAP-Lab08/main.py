from typing import List


class ChatMediator:
    def __init__(self):
        self.participants = []

    def add_participant(self, participant):
        self.participants.append(participant)

    def send_message(self, sender, recipient_name, message):
        for participant in self.participants:
            if participant.name == recipient_name:
                participant.receive_message(sender, message)
                return
        print(f"[System] {recipient_name} not found in chat.")


class Participant:
    def __init__(self, name, mediator: ChatMediator):
        self.name = name
        self.mediator = mediator
        self.mediator.add_participant(self)

    def send_message(self, recipient_name, message):
        print(f"{self.name} -> {recipient_name}: {message}")
        self.mediator.send_message(self.name, recipient_name, message)

    def receive_message(self, sender, message):
        print(f"{self.name} received from {sender}: {message}")

chat = ChatMediator()
user1 = Participant("Alice", chat)
user2 = Participant("Bob", chat)
user3 = Participant("Charlie", chat)

user1.send_message("Bob", "Привіт, Боб!")
user2.send_message("Alice", "Привіт, Аліса!")
user3.send_message("David", "Ти тут?")
