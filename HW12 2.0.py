from clases.Address_Book import AddressBook
from clases.Record import Record

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

