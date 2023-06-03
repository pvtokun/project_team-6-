from utility_func import hello_user, add_user, add_birthday, change_phone, remove_phone, show_phone, unknown_command, goodbye, paginate, search_contact_book, save, load, upcoming_birthday, add_email

HANDLERS = {
    'hello': hello_user,
    'add': add_user,
    'birthday': add_birthday,  #birthday 'name' 'birthday date'
    'change': change_phone,
    'remove': remove_phone,
    'show': show_phone,
    'find': search_contact_book,
    'save': save,
    'load': load,
    'exit': goodbye,
    'close': goodbye,
    'paginate': paginate,
    'upcoming': upcoming_birthday,
    'email': add_email
}

def main():
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
        
        handler = HANDLERS.get(command.lower())
        if args:
            args = args[0].split(' ')
        if handler:
            result = handler(*args)
        else:
            result = unknown_command(command)
        print(result)

if __name__ == '__main__':
    main()