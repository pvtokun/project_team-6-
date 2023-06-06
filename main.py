from Address_Book.function_folder.utility_func import hello_user, add_user, add_birthday, change_phone, remove_phone, show_phone, unknown_command, goodbye, paginate, search_contact_book, save, load, upcoming_birthday, add_email, change_email, remove_email
from Notes_Manager.function_folder.func_Notes import add_note, search_notes, edit_note, remove_note, show_notes
from File_Sorter.main import sorter
from pathlib import Path

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
    'close': goodbye,                   # Закриття програми
    'help': lambda: "Available commands: add, search, edit, remove, show, help",         #виводить список доступних команд для адресної книги 
}

NOTE_HANDLERS = {
    'add': add_note,
    'search': search_notes,
    'edit': edit_note,
    'remove': remove_note,
    'show': show_notes,
    'help': lambda: "Available commands: add, search, edit, remove, show, help"        #виводить список доступних команд для нотатника
}

def main():
    while True:
        print('Options:\n 1. Contact Book \n 2. Note Manager\n 3. File Sorter')
        main_input = input('Hello, choose the option: ')
        if not main_input:
            continue

        if main_input in ['close', 'exit']:
            print('Goodbye')
            break

        if main_input == '1':
            while True:
                user_input = input('Please enter command or command and args: ')
                if not user_input:
                    continue

                command, *args = user_input.strip().split(' ', 1)

                if command.lower() == 'hello':
                    hello_user()
                    continue
                if command.lower() in ['exit', 'close']:
                    goodbye()
                    break

                if command.lower() == 'change':
                    print('1. Change phone')
                    print('2. Change email')
                    change_input = input('Please choose the command: ')
                    if change_input == '1':
                        command_input = input('Enter the name, old phone, and new phone: ')
                        name, old_phone, new_phone = command_input.strip().split()
                        result = change_phone(name, old_phone, new_phone)
                        print(result)
                        continue
                    if change_input == '2':
                        command_input = input('Enter the name, old email, and new email: ')
                        name, old_email, new_email = command_input.strip().split()
                        result = change_email(name, old_email, new_email)
                        print(result)
                        continue

                if command.lower() == 'remove':
                    print('1. Remove phone')
                    print('2. Remove email')
                    change_input = input('Please choose the command: ')
                    if change_input == '1':
                        command_input = input('Enter the name and phone: ')
                        name, phone = command_input.strip().split()
                        result = remove_phone(name, phone)
                        print(result)
                        continue
                    if change_input == '2':
                        command_input = input('Enter the name and email: ')
                        name, email = command_input.strip().split()
                        result = remove_email(name, email)
                        print(result)
                        continue

                handler = HANDLERS.get(command.lower())
                if args:
                    args = args[0].split(' ')
                if handler:
                    result = handler(*args)
                else:
                    result = unknown_command(command)
                print(result)

        if main_input == '2':
            while True:
                user_input = input('Please enter command: ')
                if user_input in ['exit', 'close']:
                    goodbye()
                    break

                handler = NOTE_HANDLERS.get(user_input)
                if handler:
                    result = handler()
                else:
                    result = unknown_command(user_input)
                print(result)

        if main_input == '3':
            try:
                folder_for_scan = Path(input('Enter the path: '))
                sorter(folder_for_scan.resolve())
                print('Done')
            except FileNotFoundError:
                print('File is already sorted')


if __name__ == '__main__':
    main()
