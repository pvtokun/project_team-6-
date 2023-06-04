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

    def get_all_notes(self):
        return self.notes

