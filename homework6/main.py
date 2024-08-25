from address_book import AddressBook
from record import Record

# Створення нової адресної книги
book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
# Додавання запису Джона до адресної книги
book.add_record(john_record)
#Створення та додавання нового запису для Джейн
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)
# Друк всіх записів у книзі
for name, record in book.data.items():
    print(record)

john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)  #Вихід: Контактна особа: John, телефони: 1112223333; 5555555555
# Пошук певного номера телефону в записі Джона
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # вихід: 5555555555

book.delete("Jane")