import time


class Account:
    def __init__(self, name):
        self.name = name
        self.cards = open('cards/' + name, 'r+').readlines()
        self.created_time = time.ctime()


class Card:
    def __init__(self, owner: Account):
        self.owner = owner
        self.creating_time = time.ctime()