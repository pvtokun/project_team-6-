class Note:
    def __init__(self, title, content, tags):
        self.title = title  # Назва
        self.content = content  # Зміст
        self.tags = tags  # Теги

class NoteBook:
    index = 0
    def __init__(self):
        self.notes = []  # Пустий список нотаток
        

    def add_note(self, note):
        NoteBook.index += 1
        self.notes.append(note)  # Додавання нотатки до списку


    def edit_note(self, note_index, new_title, new_content, new_tags):
        if note_index < len(self.notes):  # Перевірка наявності нотатки з вказаним індексом
            if new_title == '' or new_content == '' or new_tags == '':
                return 'Plese enter the complet data: new title, new content and the new tags for change notes'
            elif new_title == ' ' or new_content == ' ' or new_tags == ' ':
                self.remove_note_by_index(note_index)
                return 'Notes deleted'
            else:
                note = self.notes[note_index]  # Отримання нотатки за індексом
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

    def remove_note_by_index(self,index):
        NoteBook.index -= 1
        if 0 <= index < len(self.notes):
            del self.notes[index]
            return "Note deleted successfully!"
        else:
            return "Invalid note index!"

    def get_all_notes(self):
        return self.notes  # Повертаємо всі нотатки

