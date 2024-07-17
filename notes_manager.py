import json
import os
import uuid
from datetime import datetime

class NotesManager:
    def __init__(self, filename):
        self.filename = filename
        self.load_notes()

    def load_notes(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as file:
                self.notes = json.load(file)
        else:
            self.notes = []

    def save_notes(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.notes, file, ensure_ascii=False, indent=4)

    def add_note(self, title, message):
        note = {
            'id': str(uuid.uuid4()),
            'title': title,
            'message': message,
            'timestamp': datetime.now().isoformat()
        }
        self.notes.append(note)
        self.save_notes()
        print("Заметка успешно добавлена")

    def list_notes(self, date_filter=None):
        filtered_notes = self.notes
        if date_filter:
            filtered_notes = [note for note in self.notes if note['timestamp'].startswith(date_filter)]
        
        for note in filtered_notes:
            print(f"ID: {note['id']}\nЗаголовок: {note['title']}\nДата: {note['timestamp']}\n")

    def show_note_by_id(self, note_id):
        note = next((note for note in self.notes if note['id'] == note_id), None)
        if note:
            print(f"ID: {note['id']}\nЗаголовок: {note['title']}\nДата: {note['timestamp']}\nСообщение: {note['message']}")
        else:
            print("Заметка не найдена")

    def delete_note_by_id(self, note_id):
        self.notes = [note for note in self.notes if note['id'] != note_id]
        self.save_notes()
        print("Заметка успешно удалена")

    def edit_note_by_id(self, note_id, new_title=None, new_message=None):
        note = next((note for note in self.notes if note['id'] == note_id), None)
        if note:
            if new_title:
                note['title'] = new_title
            if new_message:
                note['message'] = new_message
            note['timestamp'] = datetime.now().isoformat()
            self.save_notes()
            print("Заметка успешно отредактирована")
        else:
            print("Заметка не найдена")
