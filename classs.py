import time
import weakref


def assign_cards(account):
    cards = []
    with open('cards/' + account.name + '.txt', 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 3):
            cards.append(Card(account, lines[i + 1], lines[i + 2]))
    return cards


class Account:
    instances = []

    def __init__(self, name):
        self.name = name
        self.created_time = time.ctime()
        self.__class__.instances.append(weakref.proxy(self))
        self.cards = assign_cards(self)


class Card:
    def __init__(self, owner: Account, title, description):
        self.owner = owner
        self.creating_time = time.ctime()
        self.title = title
        self.description = description
