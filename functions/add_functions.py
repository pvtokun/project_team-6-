from clases.Record import Record
from clases.Field import Name, Birthday, Phone, Email
from utility_func import CONTACTS
from utility_func import input_error

@input_error
def add_user(name: str, phone: str = None) -> str:
    name_rec = Name(name)
    phone_rec = Phone(phone)
    phone_rec.value = phone
    record = Record(name_rec, phone_rec)
    if name not in CONTACTS.data:
        result = f'New user {name} is added!'
    else:
        return add_phone(name, phone_rec)
    CONTACTS.add_record(record)
    return result

def add_phone(name: str, phone: str) -> str:
    record = CONTACTS.get_records(name)
    record.add_phone(phone)
    CONTACTS.add_record(record)
    return f'For user {name} is added a new phone {phone}!'

@input_error
def add_birthday(name: str, birthday: Birthday) -> str:
    record = CONTACTS.data.get(name)
    if not record:
        return "Contact not found"
    try: 
        bd_date_str = Birthday(birthday)
        bd_date_str.value = birthday
        record.set_birthday(bd_date_str)
        CONTACTS.add_record(record)
        return f"Added birthday: {bd_date_str.value}"
    except ValueError:
        return f"Invalid date format. Please use the format: DD-MM-YYYY. Birthday: {bd_date_str.value}"