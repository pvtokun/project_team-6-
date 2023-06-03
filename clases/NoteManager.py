class NoteManager:
    def init(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def search_notes_by_keyword(self, keyword):
        results = []
        for note in self.notes:
            if keyword.lower() in note.text.lower() or keyword in note.tags:
                results.append(note)
        return results

    def sort_notes_by_tag(self, tag):
        results = []
        for note in self.notes:
            if tag in note.tags:
                results.append(note)
        return results

    def edit_note_text(self, note, new_text):
        note.text = new_text

    def delete_note(self, note):
        self.notes.remove(note)
