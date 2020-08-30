import time, math
from classs import Account
import sqlite3
import PySimpleGUI as gu

# Database stuff
conn = sqlite3.connect('cards.db')
c = conn.cursor()

print("\tMENU\n\tAvailable Accounts")
a = Account('ali')
b = Account("mahdi")

for counter, i in enumerate(Account.instances):
    print('   ', counter + 1, i.name)
print()

inp = int(input("\tenter account number or 0 for making new account:\t"))

if inp != 0:
    account = Account.instances[inp]
else:
    account = Account(input('\tEnter Account name:\t'))

inp = input("\tWelcome!!!\n\tAccount Menu\n\t1.make new card\n\t2.start your practice\n\tchoose:\t")
if inp == 1:
    title = input('enter title:\t')
    desc = input('enter desc:\t')
    c.execute("INSERT INTO cards VALUES (" + title + "," + desc + ")")
elif inp == 2:
    time.time()
