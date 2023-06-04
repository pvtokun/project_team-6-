from utility_func import hello_user, add_user, add_birthday, change_phone, remove_phone, show_phone, unknown_command, goodbye, paginate, search_contact_book, save, load, upcoming_birthday, add_email, change_email, remove_email

# Словник обробників команд
HANDLERS = {
    'hello': hello_user,               # Привітання користувача
    'add': add_user,                   # Додавання контакту
    'birthday': add_birthday,          # Додавання дня народження
    'email': add_email,                # Додавання емейлу
    'upcoming': upcoming_birthday,     # Відображення наближених днів народжень
    'show': show_phone,                # Показ телефону
    'find': search_contact_book,       # Пошук в контактній книзі
    'paginate': paginate,              # Розподіл на сторінки
    'save': save,                      # Збереження даних
    'load': load,                      # Завантаження даних
    'exit': goodbye,                   # Вихід з програми
    'close': goodbye                   # Закриття програми
}

def main():
    while True:
        user_input = input('Please enter command or command and args: ')  # Отримати введену користувачем команду
        if not user_input:  # Якщо введено порожній рядок, продовжити наступну ітерацію циклу
            continue

        command, *args = user_input.strip().split(' ', 1)  # Розбити введений рядок на команду та аргументи

        if command.lower() == 'hello':  # Обробка команди 'hello'
            hello_user()
            continue
        if command.lower() in ['exit', 'close']:  # Обробка команд 'exit' та 'close'
            goodbye()
            break

        if command.lower() == 'change':  # Обробка команди 'change'
            print('1. Change phone')
            print('2. Change email')
            change_input = input('Please choose the command: ')
            if change_input == '1':  # Обробка команди 'change' з варіантом '1' (зміна телефону)
                command_input = input('Enter the name, old phone, and new phone: ')
                name, old_phone, new_phone = command_input.strip().split()
                result = change_phone(name, old_phone, new_phone)
                print(result)
                continue
            if change_input == '2':  # Обробка команди 'change' з варіантом '2' (зміна електронної пошти)
                command_input = input('Enter the name, old email, and new email: ')
                name, old_email, new_email = command_input.strip().split()
                result = change_email(name, old_email, new_email)
                print(result)
                continue
        
        if command.lower() == 'remove':  # Обробка команди 'remove'
            print('1. Remove phone')
            print('2. Remove email')
            change_input = input('Please choose the command: ')
            if change_input == '1':  # Обробка команди 'remove' з варіантом '1' (видалення телефону)
                command_input = input('Enter the name and phone: ')
                name, phone = command_input.strip().split()
                result = remove_phone(name, phone)
                print(result)
                continue
            if change_input == '2':  # Обробка команди 'remove' з варіантом '2' (видалення електронної пошти)
                command_input = input('Enter the name and email: ')
                name, email = command_input.strip().split()
                result = remove_email(name, email)
                print(result)
                continue

        handler = HANDLERS.get(command.lower())  # Отримати відповідний обробник команди зі словника HANDLERS
        if args:
            args = args[0].split(' ')  # Розбити аргументи на окремі частини
        if handler:  # Якщо знайдено обробник для команди
            result = handler(*args)  # Викликати відповідний обробник з аргументами
        else:  # Якщо команда не знайдена
            result = unknown_command(command)  # Викликати функцію для обробки невідомої команди
        print(result)  # Вивести результат

if __name__ == '__main__':
    main()
