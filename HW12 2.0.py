from collections import UserDict
from datetime import datetime, timedelta
import pickle


class Field:
    def __init__(self, value=None):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not self._is_valid_phone(value):
            raise ValueError("Неправильний формат номера телефону.")
        super().__init__(value)

    def _is_valid_phone(self, value):
        # Реалізуйте логіку перевірки номера телефону тут
        # Поверніть True, якщо номер телефону є коректним, False в іншому випадку
        # Наприклад: перевірка, чи номер телефону має 10 цифр
        return len(str(value)) == 10


с
class Birthday(Field):
    def __init__(self, value):
        if not self._is_valid_birthday(value):
            raise ValueError("Неправильний формат дня народження.")
        super().__init__(value)

    def _is_valid_birthday(self, value):
        # Реалізуйте логіку перевірки дня народження тут
        # Поверніть True, якщо день народження є коректним, False в іншому випадку
        # Наприклад: перевірка, чи дата дня народження є коректною
        try:
            datetime.strptime(str(value), "%Y-%m-%d")
            return True
        except ValueError:
            return False



class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday)

    def add_phone(self, phone):
        phone_obj = Phone(phone)
        self.phones.append(phone_obj)

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone

    def days_to_birthday(self):
        if self.birthday.value:
            today = datetime.today().date()
            next_birthday = datetime(today.year, self.birthday.value.month, self.birthday.value.day).date()
            if today > next_birthday:
                next_birthday = datetime(today.year + 1, self.birthday.value.month, self.birthday.value.day).date()
            return (next_birthday - today).days


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.data, file)

    def load_from_file(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.data = pickle.load(file)
        except FileNotFoundError:
            print("Файл не знайдено. Нова адресна книга створена.")

    def search(self, search_query):
        search_results = []
        for record in self.data.values():
            if search_query in record.name.value or any(search_query in phone.value for phone in record.phones):
                search_results.append(record)
        return search_results


def main():
    address_book = AddressBook()
    address_book.load_from_file("address_book.dat")

    while True:
        print("1. Додати контакт")
        print("2. Видалити контакт")
        print("3. Редагувати контакт")
        print("4. Пошук контактів")
        print("5. Зберегти адресну книгу")
        print("6. Вийти")

        choice = input("Виберіть опцію: ")

        if choice == "1":
            name = input("Введіть ім'я: ")
            phone = input("Введіть номер телефону: ")
            birthday = input("Введіть день народження (рік-місяць-день): ")
            record = Record(name, birthday)
            record.add_phone(phone)
            address_book.add_record(record)
            print("Контакт додано!")

        elif choice == "2":
            name = input("Введіть ім'я контакту, який потрібно видалити: ")
            del address_book[name]
            print("Контакт видалено!")

        elif choice == "3":
            name = input("Введіть ім'я контакту, який потрібно редагувати: ")
            if name in address_book:
                record = address_book[name]
                new_phone = input("Введіть новий номер телефону: ")
                record.edit_phone(record.phones[0].value, new_phone)
                print("Контакт відредаговано!")
            else:
                print("Контакт не знайдено!")

        elif choice == "4":
            search_query = input("Введіть рядок для пошуку: ")
            results = address_book.search(search_query)
            if results:
                print("Результати пошуку:")
                for result in results:
                    print("Ім'я:", result.name.value)
                    print("Телефони:")
                    for phone in result.phones:
                        print(phone.value)
                    if result.birthday.value:
                        print("День народження:", result.birthday.value)
                    print("-----------------------")
            else:
                print("Збігів не знайдено.")

        elif choice == "5":
            address_book.save_to_file("address_book.dat")
            print("Адресна книга збережена!")

        elif choice == "6":
            break

        print()

if __name__ == "__main__":
    main()

