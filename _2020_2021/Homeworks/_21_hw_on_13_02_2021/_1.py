from dataclasses import dataclass
from abc import ABC, abstractmethod
import sqlite3

conn = sqlite3.connect('phones.sqlite')
cursor = conn.cursor()


@dataclass
class User:
    phone: str
    name: str
    surname: str


class AbstractUsers(ABC):
    @abstractmethod
    def add_user(self, user: User):
        pass


class Users(AbstractUsers):
    def __init__(self, data_source_url):
        self.conn = sqlite3.connect(data_source_url)
        self.cursor = self.conn.cursor()

    def add_user(self, user: User):
        self.cursor.execute(f'''INSERT INTO users VALUES ({user.phone}, {user.name}, {user.surname})''')
        self.conn.commit()


conn.commit()
cursor.close()
conn.close()
