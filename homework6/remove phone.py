import json

class PhoneBook:
    def __init__(self):
        self.phone_book = {}

    def add_phone(self, name, phone):
        if name in self.phone_book:
            self.phone_book[name].append(phone)
        else:
            self.phone_book[name] = [phone]

    def remove_phone(self, name, phone):
        # Реалізація методу для видалення номера телефону
        if name in self.phone_book:
            try:
                self.phone_book[name].remove(phone)
                if not self.phone_book[name]:  # Якщо список порожній, видаляємо ім'я
                    del self.phone_book[name]
            except ValueError:
                print(f"Номер телефону {phone} не знайдено для {name}.")
        else:
            print(f"Ім'я {name} не знайдено в телефонній книзі.")

    def show_phone_book(self):
        return json.dumps(self.phone_book, indent=4, ensure_ascii=False)


class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []  # Список номерів телефону

    def add_phone(self, phone):
        """Додає номер телефону до запису."""
        self.phones.append(phone)

    def remove_phone(self, phone):
        """Видаляє номер телефону зі списку. Якщо номера немає, виводить повідомлення."""
        try:
            self.phones.remove(phone)
        except ValueError:
            print(f"Номер телефону {phone} не знайдено в записі {self.name}.")

    def edit_phone(self, old_phone, new_phone):
        """
        Редагує номер телефону.
        Якщо старий номер не існує, викидає ValueError.
        """
        if old_phone not in self.phones:
            raise ValueError(f"Номер телефону {old_phone} не існує в записі {self.name}.")
        index = self.phones.index(old_phone)
        self.phones[index] = new_phone

    def __repr__(self):
        return f"Record(name={self.name}, phones={self.phones})"


if __name__ == "__main__":
    # Демонстрація роботи класу PhoneBook
    pb = PhoneBook()
    pb.add_phone("John", "12345")
    pb.add_phone("John", "67890")
    pb.add_phone("Jane", "54321")

    print("Телефонна книга перед видаленням:")
    print(pb.show_phone_book())

    pb.remove_phone("John", "12345")
    print("\nТелефонна книга після видалення номера 12345 для John:")
    print(pb.show_phone_book())

    pb.remove_phone("John", "11111")  # Номер не існує
    pb.remove_phone("Jake", "54321")  # Ім'я не існує

    # Демонстрація роботи класу Record та методу edit_phone
    record = Record("Alice")
    record.add_phone("11111")
    record.add_phone("22222")
    print("\nЗапис перед редагуванням:", record)
