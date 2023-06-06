# определим класс Note для заметок
from ..class_folder.class_Notes import Note, NoteBook

import pickle


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
def add_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    tags = input("Enter comma-separated tags for the note: ").split(",")
    note = Note(title, content, tags)
    notebook.add_note(note)
    return "Note added successfully!"

@input_error
def search_notes():
    tag = input("Enter tag to search notes: ")
    matching_notes = notebook.search_notes_by_tag(tag)
    if matching_notes:
        result = "Matching notes:\n"
        for note in matching_notes:
            result += f"Index note: {NoteBook.index}\nTitle: {note.title}\nContent: {note.content}\nTags: {', '.join(note.tags)}\n\n"
    else:
        result = "No notes found with the given tag."
    return result

@input_error
def show_notes():
    notes = notebook.get_all_notes()
    if notes:
        result = "Notes:\n"
        for note in notes:
            result += f"Index note: {NoteBook.index}\nTitle: {note.title}\nContent: {note.content}\nTags: {', '.join(note.tags)}\n\n"
    else:
        result = "No notes found."
    return result


@input_error
def edit_note():
    note_index = int(input("Enter the index of the note to edit: "))
    new_title = input(f"Enter new title for the note : ")
    new_content = input(f"Enter new content for the note: ")
    new_tags = input(f"Enter new comma-separated tags for the note: ")
    result = notebook.edit_note((int(note_index) - 1), new_title, new_content, new_tags)
    return result

@input_error
def remove_note():
    command_input = input("Remove by tag(all) or remove by index(single one): ")
    command_parts = command_input.strip().split()

    if len(command_parts) != 1:
        return "Invalid command format!"

    command = command_parts[0]
    result = ''
    if command.isdigit():
        result = notebook.remove_note_by_index(int(command) - 1)
    else:
        result = remove_note_by_tag(command)
    return result

def remove_note_by_tag(tag):
    matching_notes = notebook.search_notes_by_tag(tag)
    if matching_notes:
        notebook.remove_notes_by_tag(tag)
        return f"All notes with the tag '{tag}' deleted successfully!"
    else:
        return f"No notes found with the tag '{tag}'."

def save():
    with open('Notes.txt', 'wb') as file:
        pickle.dump(notebook.notes, file)  # Збереження списку контактів у файл
    return 'Contacts list saved!'

def load():
    with open('Notes.txt', 'rb') as file:
        notebook.notes = pickle.load(file)  # Завантаження списку контактів з файлу
    return 'Contacts list loaded!'