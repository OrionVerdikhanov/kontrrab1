import argparse
import sys
from notes_manager import NotesManager

def main():
    parser = argparse.ArgumentParser(description="Notes Application")
    subparsers = parser.add_subparsers(dest='command', required=True)

    add_parser = subparsers.add_parser('add', help='Добавить новую заметку')
    add_parser.add_argument('--title', required=True, help='Заголовок заметки')
    add_parser.add_argument('--msg', required=True, help='Тело заметки')

    list_parser = subparsers.add_parser('list', help='Список всех заметок')
    list_parser.add_argument('--date', help='Фильтр по дате (ГГГГ-ММ-ДД)')

    show_parser = subparsers.add_parser('show', help='Показать заметку')
    show_parser.add_argument('--id', required=True, help='ID заметки')

    delete_parser = subparsers.add_parser('delete', help='Удалить заметку')
    delete_parser.add_argument('--id', required=True, help='ID заметки')

    edit_parser = subparsers.add_parser('edit', help='Редактировать заметку')
    edit_parser.add_argument('--id', required=True, help='ID заметки')
    edit_parser.add_argument('--title', help='Новый заголовок заметки')
    edit_parser.add_argument('--msg', help='Новое тело заметки')

    args = parser.parse_args()
    manager = NotesManager('notes.json')

    if args.command == 'add':
        manager.add_note(args.title, args.msg)
    elif args.command == 'list':
        manager.list_notes(args.date)
    elif args.command == 'show':
        manager.show_note_by_id(args.id)
    elif args.command == 'delete':
        manager.delete_note_by_id(args.id)
    elif args.command == 'edit':
        manager.edit_note_by_id(args.id, args.title, args.msg)

if __name__ == "__main__":
    main()
