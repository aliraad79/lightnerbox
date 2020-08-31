import sqlite3
import time
import weakref


class Account:
    instances = []

    def __init__(self, name):
        self.name = name
        self.created_time = time.ctime()
        self.__class__.instances.append(weakref.proxy(self))
        open("cards/" + name + ".txt", 'a+')

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
