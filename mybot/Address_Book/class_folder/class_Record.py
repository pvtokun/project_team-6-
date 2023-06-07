from datetime import datetime
from ..class_folder.class_Field import Name, Phone, Birthday, Email

class Record:
    def __init__(self, name: Name, phone: Phone=None, birthday: Birthday=None, email: Email=None) -> None:
        self.name = name
        self.phones = []
        self.birthday = None
        self.email = None

        if phone is not None:
            self.add_phone(phone)

        if birthday is not None:
            self.set_birthday(birthday)
        
        if email is not None:
            self.set_email(email)

    def set_birthday(self, birthday: Birthday):
        self.birthday = birthday.value

    def remove_birthday(self):
        self.birthday = None

    def set_email(self, email: Email):
        self.email = email.value
    
    def change_email(self, old_email, new_email):
        if old_email.value == old_email:
            old_email.value = new_email
            return f'{old_email} has been changed to a new one: {new_email}'
        else:
            return f'Phone {old_email} not found'
        
    def show_email(self):
        return f'{self.email}'

    def remove_email(self):
        self.email - None

    # Перевіряємо, чи рік є високосним
    def is_leap_year(year):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                return False
            return True
        return False

    def days_to_birthday(self) -> int:
        if self.birthday is None:
            return 'please enter your date of birth'
        
        # беремо поточну дату
        current_date = datetime.now().date()

        # перевірка на правильність дати
        date_obj = datetime.strptime(self.birthday, '%d-%m-%Y').date()
        
        # перевірка на високосний рік
        if (date_obj.month, date_obj.day) == (2, 29) and not self.is_leap_year(current_date.year):
            date_obj = date_obj.replace(day=date_obj.day - 1)
        birthday = date_obj.replace(year=current_date.year)
        
        if birthday < current_date:
            birthday = birthday.replace(year=current_date.year + 1)
        
        days_to_birthday = (birthday - current_date).days
        
        return days_to_birthday
    

    # фукнціїнал отримання списку контактів у яких день народження через N кільксть днів 
    def get_upcoming_birthday(self, days):
        current_date = datetime.now().date()

        date_obj = datetime.strptime(self.birthday, '%d-%m-%Y').date()
        birthday = date_obj.replace(year=current_date.year)
        
        if birthday < current_date:
            birthday = birthday.replace(year=current_date.year + 1)
        
        if (birthday - current_date).days == days:
            return f' have birthday in {days} days'


    def add_phone(self, phone: Phone | str):
        if isinstance(phone, str):
            phone = self.create_phone(phone)
        self.phones.append(phone)
    
    def create_phone(self, phone: str):
        return Phone(phone)

    def remove_phone(self, phone):
        new_phone_list = list(filter(lambda x: str(x) != str(phone), self.phones))
        if len(new_phone_list) != len(self.phones):
            self.phones = list(new_phone_list)
            return f'phone: {phone} deleted'
        return f'phone {phone} not found'

    def change_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return f'{old_phone} has been changed to a new one: {new_phone}'
            else:
                return f'Phone {old_phone} not found'
    
    def show_phone(self):
        res = ''
        for index, phone in enumerate(self.phones):
           res += f'{index + 1}. {phone.value} '
        return res
    
    def show_birthday(self):
        if self.birthday is None:
            return 'date of birth not specified'
        return f'birthday: {self.birthday}'

    def __repr__(self) -> str:
        return f'{self.phones}'