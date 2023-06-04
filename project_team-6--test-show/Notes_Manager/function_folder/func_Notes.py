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
            result += f"Title: {note.title}\nContent: {note.content}\nTags: {', '.join(note.tags)}\n\n"
    else:
        result = "No notes found with the given tag."
    return result

@input_error
def edit_note():
    note_index = int(input("Enter the index of the note to edit: "))
    result = notebook.edit_note(note_index)
    return result




