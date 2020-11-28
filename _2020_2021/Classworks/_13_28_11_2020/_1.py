import uuid
from abc import ABC, abstractmethod, abstractclassmethod


class AbstractTask(ABC):
    @abstractmethod
    def remove_task(self):
        pass

    @abstractmethod
    def update_task_text(self, new_task_text):
        pass

    @abstractmethod
    def update_task_status(self, new_status):
        pass


class AbstractNote(ABC):
    @abstractmethod
    def remove_note(self):
        pass

    @abstractmethod
    def update_note_text(self, new_note):
        pass

    @abstractclassmethod
    def read_note(cls, note_dict):
        pass


class Note(AbstractNote):
    def __init__(self, note_text, note_id=None):
        self.note_text = note_text
        self._note_id = note_id
        if note_id is None:
            self._note_id = uuid.uuid4()
        self.note_dict = {'note_text': self.note_text,
                          'id': self._note_id}

    def remove_note(self):
        self.note_text['note_text'] = None
        self.note_text['id'] = None
        self.note_text, self._note_id = None, None

    def update_note_text(self, new_note):
        self.note_text = new_note
        self.note_text['note_text'] = self.note_text

    @classmethod
    def read_note(cls, note_dict):
        if 'text' not in note_dict.keys() or 'id' not in note_dict.keys():
            raise RuntimeError('Not all necessary keys were found in dict')
        return Task(note_dict['text'], note_dict['id'])


class Task(AbstractTask):
    def __init__(self, task_text, task_status, task_id=None):
        self.task_text = task_text
        self.task_status = task_status
        self._task_id = task_id
        if task_id is None:
            self._task_id = uuid.uuid4()
        self.task_dict = {'text': self.task_text,
                          'status': self.task_status,
                          'id': self._task_id}

    def remove_task(self):
        self.task_dict['text'] = None
        self.task_dict['status'] = None
        self.task_dict['id'] = None
        self.task_text, self.task_status, self._task_id = None, None, None

    def update_task_text(self, new_task_text):
        self.task_text = new_task_text
        self.task_dict['text'] = self.task_text

    def update_task_status(self, new_status):
        self.task_status = new_status
        self.task_dict['status'] = self.task_status

    @classmethod
    def read_task(cls, task_dict):
        if 'text' not in task_dict.keys() or 'status' not in task_dict.keys() or 'id' not in task_dict.keys():
            raise RuntimeError('Not all necessary keys were found in dict')
        return Task(task_dict['text'], task_dict['status'], task_dict['id'])
