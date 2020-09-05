from classs import Account, get_account_instances
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
list_of_accounts.extend(get_account_instances())

layout = [[sg.Text("Available Accounts")],
          [sg.Listbox(list_of_accounts, size=(30, 6))],
          [sg.Button('Ok')]]

# Create the Window
window = sg.Window('Lightner Box', layout, size=(400, 200))

# Event Loop to process "events" and get the "values" of the inputs

event, values = window.read()
if values[0] != ['new account']:
    for i in get_account_instances():
        if i == values[0][0]:
            account = Account(i)
            break
else:
    account = Account(sg.popup_get_text("Enter Account name"))

window.close()

# Create the Window
layout = [[sg.Button("make new card", key='-1-')],
          [sg.Button("start your practice(show cards)", key='-2-')],
          [sg.Button("add card to your practice", key='-3-')]]

window = sg.Window('Lightner Box', layout, finalize=True, size=(400, 200))


def get_next_index_of_table():
    cursor = sqlite3.connect('cards.db').cursor()
    cursor.execute("SELECT COUNT(*) from cards ")
    result = cursor.fetchone()
    return str(result[0] + 1)


def create_card():
    new_window = sg.Window('Create New Card', [[sg.Text('title'), sg.Input()], [sg.Text('Description'), sg.Input()],
                                               [sg.Button('confirm', key='confirm'),
                                                sg.Button('cancel', key='cancel')]])
    values1, event1 = new_window.read()
    if values1 == 'confirm':
        c.execute(
            "INSERT INTO cards VALUES ( '" + get_next_index_of_table() + "','" + event1[0] + "','" + event1[1] + "')")
        conn.commit()
    new_window.close()


def show_cards(cards):
    headings = ['ID', 'Title', 'Description']  # the text of the headings
    header = [[sg.Text('  ')] + [sg.Text(h, size=(14, 1)) for h in headings]]  # build header layout
    input_rows = [[sg.Text(cards[row1][col], size=(15, 1), pad=(0, 0)) for col in range(3)] for row1 in
                  range(len(cards))]
    button = [[sg.Button('OK')]]
    new_window = sg.Window('Your Cards', header + input_rows + button, font='Courier 12', finalize=True)
    event1, values1 = new_window.read()
    new_window.close()


def tick_cards(_table):
    headings = ['ID', 'Title', 'Description']  # the text of the headings
    header = [[sg.Text('  ')] + [sg.Text(h, size=(10, 1)) for h in headings]]  # build header layout
    rows = []
    for i in _table:
        rows += [[sg.Checkbox(''), sg.Text(i[0], size=(5, 1), pad=(0, 0)), sg.Text(i[1], size=(15, 1), pad=(0, 0)),
                  sg.Text(i[2], size=(30, 1), pad=(0, 0))]]
    button = [[sg.Button('OK')]]
    new_window = sg.Window('Your Cards', header + rows + button, font='Courier 12', finalize=True)
    event1, values1 = new_window.read()
    for i, j in values1.items():
        if j:
            account.add_card([_table[i]])
    new_window.close()


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == '-1-':
        create_card()
    elif event == '-2-':
        show_cards(account.get_cards())
    elif event == '-3-':
        table = c.execute('SELECT * FROM cards ')
        tick_cards(list(table))
