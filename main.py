import datetime
import time, math
from classs import Account
import sqlite3
import PySimpleGUI as sg

# Database stuff
conn = sqlite3.connect('cards.db')
c = conn.cursor()

# GUi stuff
sg.theme('DarkAmber')  # Add a touch of color

# All the stuff inside your window.
a = Account('ali')
b = Account("mahdi")
list_of_accounts = ['new account']
for i in Account.instances:
    list_of_accounts.append(i.name)
layout = [[sg.Text("Available Accounts")],
          [sg.Listbox(list_of_accounts , size=(30, 6))],
          [sg.Button('Ok')]]

# Create the Window
window = sg.Window('Lightner Box', layout)

# Event Loop to process "events" and get the "values" of the inputs

event, values = window.read()
if values[0] != 'new account':
    for i in Account.instances:
        if i.name == values[0]:
            account = i
            break
else:
    account = Account(input('\tEnter Account name:\t'))

window.close()
layout = [[sg.Button("make new card")],
          [sg.Button("start your practice(show cards)")],
          [sg.Button("add card to your practice")],
          [sg.Button('Ok')]]

# Create the Window
window = sg.Window('Lightner Box2', layout)


inp = int(input(
    "\tWelcome!!!\n\tAccount Menu\n\t1.make new card\n\t2.start your practice(show cards)\n\t3.add card to your practice\n\tchoose:\t"))
if inp == 1:
    title = input('enter title:\t')
    desc = input('enter desc:\t')
    c.execute("INSERT INTO cards VALUES ('" + title + "','" + desc + "')")
    conn.commit()
elif inp == 2:
    print(account.get_cards())
elif inp == 3:
    table = c.execute('SELECT * FROM cards ')
    print("enter(tick) numbers you want (with space between): ")
    for counter, row in enumerate(table):
        print(counter, row[0], row[1])
    account.add_card(list(map(int, input().split())))
