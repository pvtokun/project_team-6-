from ..class_folder.class_Record import Record
from ..class_folder.class_Field import Name, Phone, Birthday, Email
from ..class_folder.class_Address_Book import AddressBook
import pickle

CONTACTS = AddressBook()

def input_error(func):
    def inner(*args):
        try:
            result = func(*args)  # Викликати функцію з введеними аргументами
            return result
        except KeyError:
            return "No user"  # Обробка винятку KeyError
        except ValueError:
            return 'Give me name and phone please'  # Обробка винятку ValueError
        except IndexError:
            return 'Enter user name'  # Обробка винятку IndexError
        except TypeError:
            return 'Missed arguments'  # Обробка винятку TypeError
    return inner

@input_error
def add_user(name: str, phone: str = None) -> str:
    name_rec = Name(name)  # Створення об'єкту типу Name з вказаним ім'ям
    phone_rec = Phone(phone)  # Створення об'єкту типу Phone з вказаним номером телефону
    phone_rec.value = phone  # Присвоєння значення номеру телефону об'єкту типу Phone
    record = Record(name_rec, phone_rec)  # Створення запису з об'єктами Name та Phone
    if name not in CONTACTS.data:  # Перевірка, чи користувач з таким ім'ям вже існує
        result = f'New user {name} is added!'  # Якщо не існує, створити нового користувача
    else:
        return add_phone(name, phone_rec)  # Якщо існує, викликати функцію add_phone для додавання телефону
    CONTACTS.add_record(record)  # Додати запис користувача до контактів
    return result  # Повернути результат операції




def add_phone(name: str, phone: str) -> str:
    record = CONTACTS.get_records(name)  # Отримання запису користувача з вказаним ім'ям
    record.add_phone(phone)  # Додавання нового номеру телефону до запису користувача
    CONTACTS.add_record(record)  # Оновлення запису користувача в контактах
    return f'For user {name} is added a new phone {phone}!'  # Повернення повідомлення про успішне додавання телефону

@input_error
def change_phone(name, old_phone, new_phone):
    record = CONTACTS.get_records(name)  # Отримання запису користувача з вказаним ім'ям
    if not record:  # Перевірка, чи існує запис користувача
        return "Contact not found"  # Якщо запис не знайдено, повернути повідомлення про відсутність контакту
    result = record.change_phone(old_phone, new_phone)  # Зміна номеру телефону у записі користувача
    return f'{name}`s {result}'  # Повернення повідомлення про успішну зміну номеру телефону

def remove_phone(name, phone): 
    record = CONTACTS.get_records(name)  # Отримання запису користувача з вказаним ім'ям
    if not record:  # Перевірка, чи існує запис користувача
        return "Contact not found"  # Якщо запис не знайдено, повернути повідомлення про відсутність контакту
    result = record.remove_phone(phone)  # Видалення номеру телефону з запису користувача
    return f'For {name} {result}'  # Повернення повідомлення про успішне видалення телефону


def add_birthday(name: str, birthday: Birthday) -> str:
    record = CONTACTS.data.get(name)  # Отримання запису користувача з вказаним ім'ям
    if not record:  # Перевірка, чи існує запис користувача
        return "Contact not found"  # Якщо запис не знайдено, повернути повідомлення про відсутність контакту
    try: 
        bd_date_str = Birthday(birthday)  # Створення об'єкту дати на основі введеної строки
        bd_date_str.value = birthday  # Присвоєння значення дати об'єкту
        record.set_birthday(bd_date_str)  # Встановлення дати народження в записі користувача
        CONTACTS.add_record(record)  # Оновлення запису користувача в контактах
        return f"Added birthday: {bd_date_str.value}"  # Повернення повідомлення про успішне додавання дня народження
    except ValueError:
        return f"Invalid date format. Please use the format: DD-MM-YYYY."  # Повернення повідомлення про некоректний формат дати

def days_to_birthday(name: str):
    record = CONTACTS.data.get(name)  # Отримання запису користувача з вказаним ім'ям
    result = record.days_to_birthday()  # Обчислення кількості днів до дня народження
    return result  # Повернення кількості днів до дня народження

def upcoming_birthday(days) -> str:
    record = CONTACTS.data  # Отримання всіх записів користувачів
    result = ''
    for name, record in record.items():
        result += f'{name}: {record.get_upcoming_birthday(int(days))}'  # Отримання наближених днів народження для кожного користувача
    return result  # Повернення рядка з наближеними днями народження для кожного користувача


def add_email(name: str, email: Email) -> str:
    record = CONTACTS.data.get(name)  # Отримання запису користувача з вказаним ім'ям
    if not record:  # Перевірка, чи існує запис користувача
        return "Contact not found"  # Якщо запис не знайдено, повернути повідомлення про відсутність контакту
    try:
        email_rec = Email(email)  # Створення об'єкту електронної пошти на основі введеної строки
        email_rec.value = email  # Присвоєння значення електронної пошти об'єкту
        record.set_email(email_rec)  # Встановлення електронної пошти в записі користувача
        CONTACTS.add_record(record)  # Оновлення запису користувача в контактах
        return f'{email_rec.value} is added!'  # Повернення повідомлення про успішне додавання електронної пошти
    except ValueError:
        return f'Invalid email, try again! Email domain must be on of: gmail.com, yahoo.com, outlook.com, hotmail.com, icloud.com, aol.com, yandex.com, zoho.com, protonmail.com, mail.com, gmx.com'  # Повернення повідомлення про некоректну електронну пошту

@input_error
def change_email(name, old_email, new_email):
    record = CONTACTS.get_records(name)  # Отримання запису користувача з вказаним ім'ям
    if not record:  # Перевірка, чи існує запис користувача
        return "Contact not found"  # Якщо запис не знайдено, повернути повідомлення про відсутність контакту
    result = record.change_email(old_email, new_email)  # Зміна електронної пошти у записі користувача
    return f'{name}`s {result}'  # Повернення повідомлення про успішну зміну електронної пошти

@input_error
def remove_email(name, email):
    record = CONTACTS.get_records(name)  # Отримання запису користувача з вказаним ім'ям
    if not record:  # Перевірка, чи існує запис користувача
        return "Contact not found"  # Якщо запис не знайдено, повернути повідомлення про відсутність контакту
    result = record.remove_email(email)  # Видалення електронної пошти з запису користувача
    return f'For {name} {result} removed'  # Повернення повідомлення про успішне видалення електронної пошти


@input_error
def show_phone(name):
    if name == 'all':
        return show_all()
    else:
        result = ''
        record = CONTACTS.data.get(name)  # Отримання запису користувача з вказаним ім'ям
        birthday = record.show_birthday()  # Отримання дати народження з запису користувача
        email = record.show_email()  # Отримання електронної пошти з запису користувача
        if email is None:
            email = "Email not set"
        if record:  # Перевірка, чи існує запис користувача
            result = f'{name} phone number is: {record.show_phone()}, {birthday} , next birthday in: {days_to_birthday(name)} days, email: {email}'
        else:
            result = f'We dont have {name} in our list'
    return result

def show_all():
    record = CONTACTS.data
    if not record:  # Перевірка, чи існують записи користувачів
        return "No contacts found"
    result = ''
    for name, record in record.items():
        birthday = record.show_birthday()  # Отримання дати народження з запису користувача
        email = record.show_email()  # Отримання електронної пошти з запису користувача
        if email is None:
            email = "Email not set"
        result += f'{name} phone number is: {record.show_phone()}, {birthday}, next birthday in: {days_to_birthday(name)} days, email: {email}\n'
    return result

def search_contact_book(query: str) -> str:
    result = ''
    try:
        int(query)
        for name, record in CONTACTS.data.items():
            if query in CONTACTS.data.get(name):
                result += f'User: {name}, {record}\n'
    except ValueError:
        get_user = list(filter(lambda x: query.lower() in x.lower(), CONTACTS.data.keys()))  # Пошук користувачів за запитом
        for name in get_user:
            user_info = CONTACTS.data.get(name)
            result += f'User: {name}, {user_info.show_phone()}, {user_info.show_birthday()}\n'
    return result


@input_error
def paginate(page_size: int) -> str:
    result = ''
    page_size_int = int(page_size)
    for page in CONTACTS.paginate(page_size_int):  # Розбиття контактів на сторінки заданого розміру
        for name, record in page:
            result += f"{name}: {record.show_phone()}, {record.show_birthday()}\n"
        result += "---\n"
    return result

def hello_user():
    print('How can I help you?')
    return

@input_error
def unknown_command(command):
    return f'Unknown command: {command}'

def goodbye():
    print('Good bye!')
    return