# определим класс Note для заметок
from ..class_folder.class_Notes import Note, NoteBook

notebook = NoteBook()


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
def add_note_handler():
    title = input("Enter note title: ") #Запрашивает у пользователя ввод заголовка заметки и сохраняет его в переменную title.
    content = input("Enter note content: ") # Запрашивает у пользователя ввод содержимого заметки и сохраняет его в переменную content.
    tags = input("Enter comma-separated tags for the note: ").split(",") #Запрашивает у пользователя ввод тегов для заметки, разделенных запятыми, и разделяет введенные теги с помощью метода split(","), чтобы получить список тегов. Затем сохраняет список тегов в переменную tags.
    note = Note(title, content, tags) # Создает новый объект Note с использованием введенного заголовка, содержимого и списка тегов, и сохраняет его в переменную note.
    notebook.add_note(note) # Добавляет созданную заметку (note) в записную книжку (notebook), предположительно вызывая соответствующий метод add_note() в объекте notebook.
    print("Note added successfully!") # Выводит сообщение "Note added successfully!" для подтверждения, что заметка была успешно добавлена.


@input_error
def search_notes_handler():
    tag = input("Enter tag to search notes: ") #Запрашивает у пользователя ввод тега, по которому требуется выполнить поиск заметок, и сохраняет его в переменную 'tag'
    matching_notes = notebook.search_notes_by_tag(tag) #Вызывает метод search_notes_by_tag(tag) у объекта notebook для выполнения поиска заметок по введенному тегу. Результат поиска сохраняется в переменную matching_notes.
    if matching_notes: # Проверяет, если matching_notes не пустой (т.е., если найдены соответствующие заметки), то выполняет следующий блок кода. Если matching_notes пустой, блок кода пропускается.
        print("Matching notes:") # Выводит сообщение "Matching notes:" для отображения, что найдены соответствующие заметки.
        for note in matching_notes: # Запускает цикл for, который итерирует по каждой заметке в matching_notes
            print(f"Title: {note.title}") #Выводит заголовок текущей заметки (note.title) в форматированном виде, добавляя префикс "Title: "
            print(f"Content: {note.content}") # Выводит содержимое текущей заметки (note.content) в форматированном виде, добавляя префикс "Content: "
            print(f"Tags: {', '.join(note.tags)}") # Выводит теги текущей заметки (note.tags) в форматированном виде, добавляя префикс "Tags: " и используя метод join() для объединения тегов в строку, разделенную запятыми.
            print()
    else:
        print("No notes found with the given tag.") # Выводит пустую строку для создания пустой строки между выводом информации о заметках.


@input_error
def edit_note_handler():
    note_index = int(input("Enter the index of the note to edit: ")) # Запрашивает у пользователя индекс заметки, которую нужно отредактировать, и сохраняет его в переменную note_index. Индекс должен быть целым числом.
    new_title = input("Enter new title: ") # Запрашивает у пользователя новый заголовок (название) для заметки и сохраняет его в переменную new_title.
    new_content = input("Enter new content: ") # Запрашивает у пользователя новое содержимое (текст) для заметки и сохраняет его в переменную new_content.
    new_tags = input("Enter new comma-separated tags: ").split(",") # Запрашивает у пользователя новые теги для заметки, разделенные запятыми, и сохраняет их в виде списка, разбивая строку ввода с помощью метода split(","). Теги будут храниться в переменной new_tags в виде списка строк.
    result = notebook.edit_note(note_index, new_title, new_content, new_tags) # Вызывает метод edit_note объекта notebook, передавая ему аргументы note_index, new_title, new_content и new_tags. Этот метод будет выполнять редактирование заметки с указанным индексом, используя новые значения заголовка, содержимого и тегов.
    return result # Возвращает результат выполнения метода edit_note в качестве результата функции edit_note_handler(). Результат может быть разным в зависимости от реализации метода edit_note, например, сообщение об успешном редактировании или ошибку.



@input_error
def remove_note_handler():
    note_index = int(input("Enter the index of the note to delete: ")) # Запрашивает у пользователя ввод индекса заметки, которую нужно удалить, и сохраняет его в переменную note_index. Функция input() возвращает строку, поэтому мы используем int() для преобразования строки в целое число.
    result = notebook.delete_note(note_index) # Вызывает метод delete_note() у объекта notebook, передавая ему note_index в качестве аргумента. Метод delete_note() будет выполнять удаление заметки по указанному индексу и вернет результат удаления, который сохраняется в переменной result.
    print(result) # Выводит значение result, которое предположительно содержит информацию о результате удаления заметки.


@input_error
def show_notes_handler():
    notes = notebook.get_all_notes() # Вызывает метод get_all_notes() у объекта notebook для получения списка всех заметок. Результат сохраняется в переменной notes.
    if notes: # Проверяет, содержит ли переменная notes какие-либо заметки. Если список заметок не пустой (т.е. есть заметки), выполняется следующий блок кода. Если список пустой (т.е. нет заметок), блок кода после else будет выполнен.
        print("Notes:") # Выводит заголовок "Notes:", чтобы указать, что будут показаны заметки.
        for note in notes: #  Для каждой заметки в списке notes выполняется следующий блок кода. В этом блоке кода происходит вывод информации о каждой заметке, включая заголовок, содержимое и теги.
            print(f"Title: {note.title}") # Выводит заголовок текущей заметки.
            print(f"Content: {note.content}") # Выводит содержимое текущей заметки.
            print(f"Tags: {', '.join(note.tags)}") #  Выводит теги текущей заметки, объединяя их с помощью запятых и пробелов.
            print() # Выводит пустую строку для создания разделения между заметками
    else: # Если список notes пустой (т.е. нет заметок), выполняется следующий блок кода.
        print("No notes found.") # Выводит сообщение "No notes found.", чтобы указать, что нет доступных заметок для отображения.
