import sqlite3
import time
import os
from datetime import date


def get_account_instances():
    temp = []
    for i in os.listdir("cards/"):
        temp.append(i.replace('.db', ''))
    return temp


class Account:

    def __init__(self, name):
        self.name = name
        self.created_time = time.ctime()
        if not os.path.exists('cards/' + name + '.txt'):
            open('cards/' + name + ".db", 'w')
            conn = sqlite3.connect('cards/' + name + '.db')
            conn.cursor().execute("CREATE TABLE " + name + " (id int PRIMARY KEY,last_read date)")
            conn.commit()

    def get_cards(self):
        return list(sqlite3.connect('cards.db').cursor().execute(
            "SELECT * FROM cards WHERE id IN (" + ", ".join(self.get_current_cards()) + ")"))

    def add_card(self, _list):
        conn = sqlite3.connect('cards/' + self.name + '.db')
        cursor = conn.cursor()
        for i in _list:
            cursor.execute("INSERT INTO " + self.name + " VALUES  (" + str(i[0]) + " ," + str(date.today()) + ")")
        conn.commit()

    def get_current_cards(self):
        return [str(i[0]) for i in sqlite3.connect("cards/" + self.name + '.db').cursor().execute(
            "SELECT id FROM " + self.name).fetchall()]
