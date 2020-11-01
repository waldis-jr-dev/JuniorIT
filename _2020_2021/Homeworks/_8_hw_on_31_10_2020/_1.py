from _2020_2021.Classworks._8_24_10_2020._2 import Passenger
import sqlite3
from typing import Union

conn = sqlite3.connect('customers.sqlite3')
cursor = conn.cursor()
cursor.executescript('''PRAGMA foreign_keys = ON''')


class Customer:
    @classmethod
    def find_customer(cls, u_id: int) -> Union[str, Passenger]:
        sql = '''SELECT id, name, birth_year, start_location, end_location, distance FROM customers WHERE id LIKE ?'''
        data = cursor.execute(sql, (u_id,)).fetchall()
        if len(data) == 0:
            return 'No customer with this ID !'
        else:
            data = data[0]
        customer = Passenger()
        customer.insert_data(id=u_id,
                             name=data[1],
                             birth_year=data[2],
                             start_location=data[3],
                             end_location=data[4],
                             distance=data[5])
        return customer

    @classmethod
    def insert_cost(cls, customer: Passenger):
        sql = '''INSERT INTO cost (customer_id, cost) VALUES (?,?)'''
        val = (customer.id, customer.price_for_km())
        cursor.execute(sql, val)
        conn.commit()


if __name__ == '__main__':
    test = Customer()
    customer1 = test.find_customer(int(input('Enter customer ID: ')))
    print(customer1)
    test.insert_cost(customer1)

cursor.close()
conn.close()
