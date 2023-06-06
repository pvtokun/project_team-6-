from re import match
from datetime import datetime

class Field:
    def __init__(self, value) -> None:
        self.value = value

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, new_value):
        self.validator(new_value)
        self.__value = new_value
    
    def validator(self, value):
        pass

class Name(Field):
    def __init__(self, value) -> None:
        super().__init__(value)

    def __repr__(self) -> str:
        return f"{self.value}"

class Phone(Field):
    def __init__(self, value) -> None:
        super().__init__(value)
 
    def validator(self, new_value):
        if isinstance(new_value, str):
            if not match(r'^\+38\d{10}$', new_value):
                print("Phone number should be in the format +380XXXXXXXXX")
                raise ValueError("Phone number should be in the format +380XXXXXXXXX")
        else:
            raise ValueError('value must be str not int')
            
    def __repr__(self) -> str:
        return f"{self.value}"

class Birthday(Field):
    def __init__(self, value) -> None:
        super().__init__(value)

    def validator(self, new_value):
        if not isinstance(new_value, str):
            raise ValueError
        try:
            datetime.strptime(new_value, '%d-%m-%Y')
        except ValueError:
            raise ValueError

class Email(Field):
    # Список допустимих емейл-доменів
    email_domains = [
        'gmail.com',
        'yahoo.com',
        'outlook.com',
        'hotmail.com',
        'icloud.com',
        'aol.com',
        'yandex.com',
        'zoho.com',
        'protonmail.com',
        'mail.com',
        'gmx.com'
    ]

    def __init__(self, value):
        super().__init__(value)

    def validator(self, new_value):
        if isinstance(new_value, str):
            parts = new_value.split('@')

            local_part, domain_part = parts

            if domain_part not in self.email_domains or local_part == '':
                # Помилка: непідтримуваний домен емейлу
                raise ValueError("Непідтримуваний домен емейлу")
        else:
            # Помилка: значення не є рядком
            raise ValueError("Значення не є рядком")

