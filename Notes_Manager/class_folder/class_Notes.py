class Note:
    def __init__(self, title, content, tags):
        self.title = title  # Назва
        self.content = content  # Зміст
        self.tags = tags  # Теги

class NoteBook:
    def __init__(self):
        self.notes = []  # Пустий список нотаток

    def add_note(self, note):
        self.notes.append(note)  # Додавання нотатки до списку

    def edit_note(self, note_index):
        if note_index < len(self.notes):  # Перевірка наявності нотатки з вказаним індексом
            note = self.notes[note_index]  # Отримання нотатки за індексом
            new_title = input(f"Enter new title for the note '{note.title}': ")
            new_content = input(f"Enter new content for the note '{note.content}': ")
            new_tags = input(f"Enter new comma-separated tags for the note '{', '.join(note.tags)}': ").split(",")
            note.title = new_title  # Зміна назви нотатки
            note.content = new_content  # Зміна змісту нотатки
            note.tags = new_tags  # Зміна тегів нотатки
            return "Note edited successfully!"
        else:
            return "Invalid note index!"

    def search_notes_by_tag(self, tag):
        result = []
        for note in self.notes:
            if tag in note.tags:  # Перевірка, чи містить нотатка заданий тег
                result.append(note)  # Додавання нотатки до результату
        return result  # Повертаємо список знайдених нотаток

    def remove_notes_by_tag(self, tag):
        removed_notes = []  # Список видалених нотаток
        for note in self.notes:
            if tag in note.tags:  # Перевірка, чи містить нотатка заданий тег
                removed_notes.append(note)  # Додавання нотатки до списку видалених
        self.notes = [note for note in self.notes if tag not in note.tags]  # Видалення нотаток зі списку
        return removed_notes  # Повертаємо список видалених нотаток

    def get_all_notes(self):
        return self.notes  # Повертаємо всі нотатки

