# Клас для представлення аудіо запису
class AudioRecord:
    def __init__(self, title, artist, duration):
        self.title = title  # Назва аудіо запису
        self.artist = artist  # Виконавець
        self.duration = duration  # Тривалість запису в секундах

    def __str__(self):
        return f"'{self.title}' by {self.artist}, duration: {self.duration}s"


# Клас колекції аудіо записів
class AudioCollection:
    def __init__(self):
        self.records = []  # Список аудіо записів

    # Метод для додавання аудіо запису
    def add_record(self, record):
        self.records.append(record)
        print(f"Record '{record.title}' added to collection.")

    # Метод для пошуку аудіо запису за назвою
    def find_record(self, title):
        for record in self.records:
            if record.title == title:
                return record
        return None

    # Метод для видалення аудіо запису за назвою
    def remove_record(self, title):
        record = self.find_record(title)
        if record:
            self.records.remove(record)
            print(f"Record '{title}' removed from collection.")
        else:
            print(f"Record '{title}' not found in collection.")

    # Метод для перегляду всіх аудіо записів
    def view_all_records(self):
        if not self.records:
            print("No records in the collection.")
        else:
            print("\n--- Audio Records ---")
            for record in self.records:
                print(record)


# Проксі-клас для доступу до колекції аудіо записів
class AudioCollectionProxy:
    def __init__(self, audio_collection=None):
        self.audio_collection = audio_collection  # Колекція, до якої надається доступ

    # Метод для підключення колекції до проксі
    def set_collection(self, audio_collection):
        self.audio_collection = audio_collection

    # Проксі-метод для додавання запису
    def add_record(self, title, artist, duration):
        if self.audio_collection:
            new_record = AudioRecord(title, artist, duration)
            self.audio_collection.add_record(new_record)
        else:
            print("Collection is not connected to proxy.")

    # Проксі-метод для пошуку запису
    def find_record(self, title):
        if self.audio_collection:
            record = self.audio_collection.find_record(title)
            if record:
                print(f"Record found: {record}")
            else:
                print(f"Record '{title}' not found in collection.")
            return record
        else:
            print("Collection is not connected to proxy.")
            return None

    # Проксі-метод для видалення запису
    def remove_record(self, title):
        if self.audio_collection:
            self.audio_collection.remove_record(title)
        else:
            print("Collection is not connected to proxy.")

    # Проксі-метод для перегляду всіх записів
    def view_all_records(self):
        if self.audio_collection:
            self.audio_collection.view_all_records()
        else:
            print("Collection is not connected to proxy.")


# Функція для створення нового запису через інтерфейс користувача
def create_record(proxy):
    title = input("Enter the title of the audio record: ")
    artist = input("Enter the artist of the audio record: ")
    try:
        duration = int(input("Enter the duration of the audio record (in seconds): "))
        proxy.add_record(title, artist, duration)
    except ValueError:
        print("Invalid duration. Please enter a valid number.")


# Функція для перегляду всіх записів
def view_records(proxy):
    proxy.view_all_records()


# Функція для пошуку запису через інтерфейс користувача
def search_record(proxy):
    title = input("Enter the title of the audio record to search for: ")
    proxy.find_record(title)


# Функція для видалення запису через інтерфейс користувача
def delete_record(proxy):
    title = input("Enter the title of the audio record to delete: ")
    proxy.remove_record(title)


# Функція для заповнення колекції кількома готовими записами
def fill_collection(proxy):
    records = [
        AudioRecord("Song One", "Artist A", 210),
        AudioRecord("Song Two", "Artist B", 180),
        AudioRecord("Song Three", "Artist C", 240),
        AudioRecord("Song Four", "Artist D", 200)
    ]

    for record in records:
        proxy.add_record(record.title, record.artist, record.duration)


# Функція для відображення меню та взаємодії з користувачем
def menu():
    collection = AudioCollection()  # Створюємо колекцію
    proxy = AudioCollectionProxy(collection)  # Підключаємо колекцію до проксі

    # Заповнюємо колекцію кількома готовими записами
    fill_collection(proxy)

    while True:
        print("\n--- Audio Collection Menu ---")
        print("1. Add audio record")
        print("2. Search for audio record")
        print("3. Delete audio record")
        print("4. View all audio records")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        if choice == '1':
            create_record(proxy)
        elif choice == '2':
            search_record(proxy)
        elif choice == '3':
            delete_record(proxy)
        elif choice == '4':
            view_records(proxy)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")


# Запуск програми
if __name__ == "__main__":
    menu()
