from phone import Phone
from name import Name

class Record:
    """Represents a contact record containing a name and a list of phone numbers."""
    
    def __init__(self, name):
        """Initialize the Record with a name and an empty list of phones."""
        self.name = Name(name)
        self.phones = []
    
    def __str__(self):
        """Return a string representation of the Record."""
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    def add_phone(self, number: str):
        """Add a phone number to the record."""
        self.phones.append(Phone(number))
    
    def remove_phone(self, number: str):
        """Remove a phone number from the record."""
        # Можна змінити реалізацію, якщо потрібно видалити лише перше входження або всі входження
        self.phones = [phone for phone in self.phones if phone.value != number]
    
    def edit_phone(self, old_number, new_number):
        """Edit a phone number in the record.
        
        Якщо старий номер не існує, викидає ValueError.
        """
        found = False
        new_phones = []
        for phone in self.phones:
            if phone.value == old_number:
                new_phones.append(Phone(new_number))
                found = True
            else:
                new_phones.append(phone)
        if not found:
            raise ValueError(f"Номер телефону {old_number} не знайдено в записі {self.name.value}.")
        self.phones = new_phones
    
    def find_phone(self, number):
        """Find a phone number in the record."""
        for phone in self.phones:
            if phone.value == number:
                return phone
