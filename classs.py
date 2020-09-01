import sqlite3
import time
import weakref
import os


class Account:

    def __init__(self, name):
        print(name)
        self.name = name
        self.created_time = time.ctime()
        if not os.path.exists('cards/' + name + '.txt'):
            open('cards/' + "accounts.txt", 'a+').write(name + '\n')
            open('cards/' + name + ".txt", 'a+')

    def get_cards(self):
        return list(sqlite3.connect('cards.db').cursor().execute(
            "SELECT * FROM cards WHERE id IN (" + ", ".join(self.get_current_cards()) + ")"))

    def add_card(self, _list):
        temp = self.get_current_cards()
        print(temp)
        temp.extend([str(i[0]).strip() for i in _list])
        open("cards/" + self.name + ".txt", 'w').write(', '.join(temp))

    def get_current_cards(self):
        t = open("cards/" + self.name + ".txt", 'r').read().split(',')
        print(t)
        if t != ['']:
            return t
        else:
            return []

    def get_instances():
        return open('cards/' + "accounts.txt", 'r').readlines()
