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

    def edit_phone(self, name, old_phone, new_phone):
        """
        Редагує номер телефону для заданого імені.
        Якщо ім'я існує, але старий номер відсутній, викидається ValueError.
        """
        if name not in self.phone_book:
            print(f"Ім'я {name} не знайдено в телефонній книзі.")
            return
        
        if old_phone not in self.phone_book[name]:
            raise ValueError(f"Номер телефону {old_phone} не існує для {name}.")

        index = self.phone_book[name].index(old_phone)
        self.phone_book[name][index] = new_phone

    def show_phone_book(self):
        return json.dumps(self.phone_book, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    # Демонстрація роботи класу PhoneBook
    pb = PhoneBook()
    pb.add_phone("John", "12345")
    pb.add_phone("John", "67890")
    pb.add_phone("Jane", "54321")

    print("Телефонна книга перед операціями:")
    print(pb.show_phone_book())

    # Видалення номера телефону
    pb.remove_phone("John", "12345")
    print("\nТелефонна книга після видалення номера 12345 для John:")
    print(pb.show_phone_book())

    # Спроба редагування неіснуючого номера телефону для John
    try:
        pb.edit_phone("John", "11111", "55555")
    except ValueError as e:
        print("\nВиключення при редагуванні:", e)

    # Редагування існуючого номера телефону
    pb.edit_phone("John", "67890", "99999")
    print("\nТелефонна книга після редагування номера для John:")
    print(pb.show_phone_book())
