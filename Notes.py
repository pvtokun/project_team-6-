# определим класс Note для заметок

class Note:
    def __init__(self, title, content, tags):
        self.title = title # Назввание
        self.content = content # Содержание
        self.tags = tags # Теги

# класс NoteBook определим для управления заметками

class NoteBook:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def edit_note(self, note_index):
        if note_index < len(self.notes):
            note = self.notes[note_index]
            new_title = input(f"Enter new title for the note '{note.title}': ")
            new_content = input(f"Enter new content for the note '{note.content}': ")
            new_tags = input(f"Enter new comma-separated tags for the note '{', '.join(note.tags)}': ").split(",")
            note.title = new_title
            note.content = new_content
            note.tags = new_tags
            return "Note edited successfully!"
        else:
            return "Invalid note index!"

    def search_notes_by_tag(self, tag):
        result = []
        for note in self.notes:
            if tag in note.tags:
                result.append(note)
        return result


notebook = NoteBook()


def add_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    tags = input("Enter comma-separated tags for the note: ").split(",")
    note = Note(title, content, tags)
    notebook.add_note(note)
    return "Note added successfully!"


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

def edit_note():
    note_index = int(input("Enter the index of the note to edit: "))
    action = input("Enter 'e' to edit the note or 'd' to delete the note: ")
    if action.lower() == 'e':
        result = notebook.edit_note(note_index)
    elif action.lower() == 'd':
        result = notebook.delete_note(note_index)
    else:
        result = "Invalid action!"
    return result

    def delete_note(self, note_index):
        if note_index < len(self.notes):
            del self.notes[note_index]
            return "Note deleted successfully!"
        else:
            return "Invalid note index!"
