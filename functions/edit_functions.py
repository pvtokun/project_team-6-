from utility_func import CONTACTS
from utility_func import input_error

@input_error
def change_phone(name, old_phone, new_phone):
    record = CONTACTS.get_records(name)
    if not record:
        return "Contact not found"
    result = record.change_phone(old_phone, new_phone)  
    return f'{name}`s {result}'

def remove_phone(name, phone): 
    record = CONTACTS.get_records(name)
    if not record:
        return "Contact not found"
    result = record.remove_phone(phone)
    return f'For {name} {result}'