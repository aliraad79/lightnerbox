import time, math
from classs import Account

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
    pass  # go
elif inp == 2:
    time
