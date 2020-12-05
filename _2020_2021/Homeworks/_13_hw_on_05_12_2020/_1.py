from abc import ABC, abstractmethod
from typing import Union, Generator
import sqlite3
import random

conn = sqlite3.connect('fighters.sqlite3')
cursor = conn.cursor()
cursor.executescript('''PRAGMA foreign_keys = ON''')


class AbstractFighter(ABC):
    @abstractmethod
    def get_fighter_id(self) -> int:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_damage(self) -> Union[int, float]:
        pass

    @abstractmethod
    def get_hp(self) -> Union[int, float]:
        pass

    @abstractmethod
    def get_strength(self) -> Union[int, float]:
        pass

    @abstractmethod
    def get_agility(self) -> Union[int, float]:
        pass

    @abstractmethod
    def attack(self, enemy):
        pass

    @abstractmethod
    def combat_history(self) -> str:
        pass

    @abstractmethod
    def heal(self, new_hp: Union[int, float]):
        pass

    @abstractmethod
    def deal_damage(self, minus_hp: Union[int, float]):
        pass

    @abstractmethod
    def add_win(self):
        pass

    @abstractmethod
    def add_loss(self):
        pass


class Fighter(AbstractFighter):
    def __init__(self,
                 name: Union[str] = None,
                 damage: Union[int, float] = None,
                 hp: Union[int, float] = None,
                 strength: Union[int, float] = None,
                 agility: Union[int, float] = None,
                 fighter_id: int = None,
                 create_new: bool = True):
        if create_new:
            sql = '''INSERT INTO fighters (name, damage, hp, MAX_HP, strength, agility) VALUES (?,?,?,?,?,?)'''
            cursor.execute(sql, (name, damage, hp, hp, strength, agility))
            conn.commit()
            self.__fighter_id = cursor.lastrowid
            self.__name = name
            self.__damage = damage
            self.__hp = hp
            self.__MAX_HP = hp 
            self.__strength = strength
            self.__agility = agility
            self.__wins = 0
            self.__losses = 0
        if not create_new:
            sql = '''SELECT name, damage, hp, MAX_HP, strength, agility, wins, losses 
                     FROM fighters WHERE fighter_id = ?'''
            fighter = cursor.execute(sql, (fighter_id,)).fetchall()[0]
            conn.commit()
            self.__fighter_id = fighter_id
            self.__name = fighter[0]
            self.__damage = fighter[1]
            self.__hp = fighter[2]
            self.__MAX_HP = fighter[3]
            self.__strength = fighter[4]
            self.__agility = fighter[5]
            self.__wins = fighter[6]
            self.__losses = fighter[7]

    def get_fighter_id(self) -> int:
        return self.__fighter_id

    def get_name(self) -> str:
        return self.__name

    def get_damage(self) -> Union[int, float]:
        return self.__damage

    def get_hp(self) -> Union[int, float]:
        return self.__hp

    def get_strength(self) -> Union[int, float]:
        return self.__strength

    def get_agility(self) -> Union[int, float]:
        return self.__agility

    def attack(self, enemy):
        if int(random.random() * 100) <= 100 - (enemy.get_strength() + enemy.get_agility()):
            enemy.deal_damage(self.get_damage())
            return True
        return False

    def combat_history(self) -> str:
        return f'Name: {self.__name}\n' \
               f'Wins: {self.__wins}\n' \
               f'Losses: {self.__losses}'

    def heal(self, new_hp: Union[int, float]):
        self.__hp = self.__MAX_HP if self.__hp + new_hp > self.__MAX_HP else self.__hp + new_hp
        sql = '''UPDATE fighters SET hp = ? WHERE fighter_id = ?'''
        cursor.execute(sql, (self.__hp, self.__fighter_id))
        conn.commit()

    def deal_damage(self, minus_hp: Union[int, float]):
        self.__hp = 0 if self.__hp - minus_hp < 0 else self.__hp - minus_hp
        sql = '''UPDATE fighters SET hp = ? WHERE fighter_id = ?'''
        cursor.execute(sql, (self.__hp, self.__fighter_id))
        conn.commit()

    def add_win(self):
        self.__wins += 1
        sql = '''UPDATE fighters SET wins = ? WHERE fighter_id = ?'''
        cursor.execute(sql, (self.__wins, self.__fighter_id))
        conn.commit()

    def add_loss(self):
        self.__losses += 1
        sql = '''UPDATE fighters SET losses = ? WHERE fighter_id = ?'''
        cursor.execute(sql, (self.__losses, self.__fighter_id))
        conn.commit()


def battle(fighter1: Fighter, fighter2: Fighter) -> Generator[str, None, None]:
    if fighter1.get_hp() == 0:
        yield f'{fighter1.get_name()} is dead and can\'t fight.'
        return
    if fighter2.get_hp() == 0:
        yield f'{fighter2.get_name()} is dead and can\'t fight.'
        return
    fighters = (fighter1, fighter2)
    ch = random.randint(0, 1)
    while fighter1.get_hp() != 0 and fighter2.get_hp() != 0:
        if fighters[ch].attack(fighters[(ch + 1) % 2]):
            yield f'{fighters[ch].get_name()} makes {fighters[ch].get_damage()} ' \
                  f'damage to {fighters[(ch+1)%2].get_name()}'
        else:
            yield f'{fighters[ch].get_name()} attack missed'
        yield f'{fighter1.get_name()} hp: {fighter1.get_hp()}; ' \
              f'{fighter2.get_name()} hp: {fighter2.get_hp()}'
        ch += 1
        ch %= 2
    if fighter1.get_hp() == 0:
        battle_log(winner=fighter2.get_fighter_id(), loser=fighter1.get_fighter_id())
        fighter2.add_win()
        fighter1.add_loss()
        yield f"{fighter2.get_name()} has won !"
    if fighter2.get_hp() == 0:
        battle_log(winner=fighter1.get_fighter_id(), loser=fighter2.get_fighter_id())
        fighter1.add_win()
        fighter2.add_loss()
        yield f"{fighter1.get_name()} has won !"


def battle_log(winner: int, loser: int):
    sql = '''INSERT INTO battles (winner, loser) VALUES (?,?)'''
    cursor.execute(sql, (winner, loser))
    conn.commit()


if __name__ == '__main__':
    # test_fighter1 = Fighter('Killer', 20, 100, 20, 15)
    # test_fighter2 = Fighter('Angel', 25, 95, 25, 20)
    test_fighter1 = Fighter(create_new=False, fighter_id=1)
    test_fighter2 = Fighter(create_new=False, fighter_id=2)
    # test_fighter1.heal(85)
    for act in battle(test_fighter1, test_fighter2):
        print(act)

cursor.close()
conn.close()
