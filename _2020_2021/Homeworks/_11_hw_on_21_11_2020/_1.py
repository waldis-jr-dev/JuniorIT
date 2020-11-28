import time
import sqlite3
from abc import ABC, abstractmethod

conn = sqlite3.connect('notes.sqlite3')
cursor = conn.cursor()
cursor.executescript('''PRAGMA foreign_keys = ON''')


class AbstractBooks(ABC):

    @abstractmethod
    def delete_book(self):
        pass

    @abstractmethod
    def book_content(self):
        pass

    @abstractmethod
    def change_book_name(self, new_name):
        pass


class AbstractNotes(ABC):
    @abstractmethod
    def delete_note(self):
        pass

    @abstractmethod
    def note_content(self):
        pass

    @abstractmethod
    def change_note_name(self, new_name):
        pass
    

class AbstractTasks(ABC):
    @abstractmethod
    def delete_task(self):
        pass

    @abstractmethod
    def task_content(self):
        pass

    @abstractmethod
    def change_task_name(self, new_name):
        pass

    @abstractmethod
    def change_task_status(self, status):
        pass


class Books(AbstractBooks):
    def __init__(self, book_name=None, book_id=None, create_new=True):
        if create_new:
            sql = '''INSERT INTO books (book_name, book_creation_time) VALUES (?,?)'''
            cursor.execute(sql, (book_name, time.time()))
            conn.commit()
            self.book_id = cursor.lastrowid
        if not create_new:
            self.book_id = book_id

    @classmethod
    def get_book_by_id(cls, book_id):
        return Books(book_id=book_id, create_new=False)

    def book_info(self):
        sql = '''SELECT book_id, book_name, book_creation_time FROM books WHERE book_id LIKE ?'''
        return cursor.execute(sql, (self.book_id,)).fetchall()

    def delete_book(self):
        sql = '''DELETE FROM books WHERE book_id LIKE ?'''
        cursor.execute(sql, (self.book_id,))
        conn.commit()

    def book_content(self):
        sql = '''SELECT note_id FROM notes WHERE book_id LIKE ?'''
        notes = []
        for note in cursor.execute(sql, (self.book_id,)).fetchall():
            notes.append(Notes(note_id=note[0], create_new=False))
        return notes

    def change_book_name(self, new_name):
        sql = '''UPDATE books SET book_name = ? WHERE book_id LIKE ?'''
        cursor.execute(sql, (new_name, self.book_id,))
        conn.commit()

    def create_note(self, note_name):
        return Notes(note_name=note_name, book_id=self.book_id)


class Notes(AbstractNotes):
    def __init__(self, note_name=None, book_id=None, note_id=None, create_new=True):
        if create_new:
            sql = '''INSERT INTO notes (book_id, note_name, note_creation_time) VALUES (?,?,?)'''
            cursor.execute(sql, (book_id, note_name, time.time()))
            conn.commit()
            self.note_id = cursor.lastrowid
        if not create_new:
            self.note_id = note_id

    @classmethod
    def get_note_by_id(cls, book_id):
        return Notes(book_id=book_id, create_new=False)

    def note_info(self):
        sql = '''SELECT note_id, book_id, note_name, note_creation_time FROM notes WHERE note_id LIKE ?'''
        return cursor.execute(sql, (self.note_id,)).fetchall()

    def delete_note(self):
        sql = '''DELETE FROM notes WHERE note_id LIKE ?'''
        cursor.execute(sql, (self.note_id,))
        conn.commit()

    def note_content(self):
        sql = '''SELECT task_id, note_id, task_name, task_creation_time, status FROM tasks WHERE note_id LIKE ?'''
        return cursor.execute(sql, (self.note_id,)).fetchall()

    def change_note_name(self, new_name):
        sql = '''UPDATE notes SET note_name = ? WHERE note_id LIKE ?'''
        cursor.execute(sql, (new_name, self.note_id,))
        conn.commit()

    def create_task(self, task_name):
        return Tasks(task_name, self.note_id)


class Tasks(AbstractTasks):
    def __init__(self, task_name, note_id):
        sql = '''INSERT INTO tasks (note_id, task_name, task_creation_time) VALUES (?,?,?)'''
        cursor.execute(sql, (note_id, task_name, time.time()))
        conn.commit()
        self.task_id = cursor.lastrowid

    def delete_task(self):
        sql = '''DELETE FROM tasks WHERE note_id LIKE ?'''
        cursor.execute(sql, (self.tasks_id,))
        conn.commit()

    def task_content(self):
        sql = '''SELECT task_id, note_id, task_name, task_creation_time, status FROM tasks WHERE task_id LIKE ?'''
        return cursor.execute(sql, (self.task_id,)).fetchall()

    def change_task_name(self, new_name):
        sql = '''UPDATE tasks SET task_name = ? WHERE task_id LIKE ?'''
        cursor.execute(sql, (new_name, self.task_id,))
        conn.commit()

    def change_task_status(self, status):
        sql = '''UPDATE tasks SET status = ? WHERE task_id LIKE ?'''
        cursor.execute(sql, (status, self.task_id))
        conn.commit()


if __name__ == '__main__':
    first_book = Books.get_book_by_id(1)
    print(first_book.book_info())
    print(first_book.book_content())


cursor.close()
conn.close()
