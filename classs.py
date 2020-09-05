import sqlite3
import time
import os
from datetime import date, datetime


def get_account_instances():
    temp = []
    for i in os.listdir("cards/"):
        temp.append(i.replace('.db', ''))
    return temp


class Account:

    def __init__(self, name):
        self.name = name
        self.created_time = time.ctime()
        if not os.path.exists('cards/' + name + '.db'):
            open('cards/' + name + ".db", 'w')
            conn = sqlite3.connect('cards/' + name + '.db')
            conn.cursor().execute("CREATE TABLE " + name + " (id int PRIMARY KEY,last_read DATE)")
            conn.commit()

    def get_must_read_cards(self):
        pass

    def get_cards(self):
        cards = {i[0]: i[1] for i in self.get_current_cards()}
        temp_list = []
        for i in sqlite3.connect('cards.db').cursor().execute(
                "SELECT * FROM cards WHERE id IN (" + ", ".join(cards.keys()) + ")").fetchall():
            temp_list.append(list(i) + [cards[str(i[0])]])
        return temp_list

    def add_card(self, card_id):
        conn = sqlite3.connect('cards/' + self.name + '.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO " + self.name + " VALUES  (" + str(card_id[0]) + " , '" + str(date.today()) + "')")
        conn.commit()

    def get_current_cards(self):
        return [(str(i[0]), datetime.strptime(str(i[1]), '%Y-%m-%d')) for i in
                sqlite3.connect("cards/" + self.name + '.db').cursor().execute(
                    "SELECT * FROM " + self.name).fetchall()]
