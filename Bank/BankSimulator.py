print('Welcome to your Simple Bank Simulator')
account_balance = '$0.00'
balance = float(account_balance.replace("$", ""))

print(f'Your balance is: {account_balance}')

action = ['Deposit', 'Withdraw', 'Check Balance', 'Quit']
print('Choose an action:')

for index, i in enumerate(action):
    print(index + 1, i)

def deposit(amount):
    global balance
    amount = float(input('Enter the amount to deposit: '))
    balance += amount
    print(f'Deposited ${balance:.2f}')

def withdraw(amount):
    global balance
    amount = float(input('Enter amount to withdraw: '))
    if amount > balance:
        print('Insufficient funds')
    else:
        balance -= amount
        print(f'Withdrew ${balance:.2f}')


def check_balance(amount):
    global balance
    print(f'Your balance is: ${balance:.2f}')


while True:
    choice = input('Enter choice: ')
    if choice == '1':
        deposit(balance)
    elif choice =='2':
        withdraw(balance)
        continue
    elif choice == '3':
        check_balance(balance)
    elif choice == '4':
        print('Thanks for using the Bank Simulator!')
        break
    else:
        print('Your input is not one of our available choices.')



