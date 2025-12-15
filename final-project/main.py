from data_manager import DataManager
from bank_account_management import BankAccountManagement

dm = DataManager()
try: 
    accounts = dm.get()
except:
    accounts = dict()
    
bam = BankAccountManagement(accounts)

def show_menu():
    print('\n------------------')
    print('1- Show All')
    print('2- Add user')
    print('3- Transfer')
    print('4- Deposit')
    print('5- Withdraw')
    print('6- Deactivate user')
    print('7- Exit')
    print('\n')

def add_user():
    while True:
        name = input('Insert name: ')
        if not name.isalpha():
            print("Name must contain only letters! Try again.")
            continue
        break
    first_amount = input('Insert amount: ')
    result = bam.add_user(name, first_amount)
    if result['status'] == 'ok':
        dm.set(accounts)
        print(f"{name} is added successfully.")
    if result['status'] == 'error':
        print(result['msg'])

def show_user_ids_and_balance():
    if not bam.accounts:
        print("No users found.")
        return
    print("User IDs, Names and Balances:")
    for user_id, info in bam.accounts.items():
        status = info.get('status', 'Active')
        status_display = f"({status.capitalize()})" if status != 'active' else ""
        print(f"{user_id} - {info['name']} {status_display} - Balance: {info['balance']}")

def transfer():
    show_user_ids_and_balance()
    from_who = input('From who? (ID): ')
    if bam.accounts.get(from_who, {}).get('status', 'active') != 'active':
        print('Sender user is deactivated, operation not allowed.')
        return
    to_whom = input('To whom? (ID): ')
    if bam.accounts.get(to_whom, {}).get('status', 'active') != 'active':
        print('Recipient user is deactivated, operation not allowed.')
        return
    amount = input('Amount: ')
    result = bam.transfer(from_who, to_whom, amount)
    if result['status'] == 'error':
        print(result['msg'])
    else:
        dm.set(accounts)
        from_name = bam.accounts[str(from_who)]['name']
        to_name = bam.accounts[str(to_whom)]['name']
        print(f"Successfully transferred {amount} $ from {from_name} to {to_name}.")

def deposit():
    show_user_ids_and_balance()
    to_who = input('To who? (ID): ')
    if bam.accounts.get(to_who, {}).get('status', 'active') != 'active':
        print('Deposit user is deactivated, operation not allowed.')
        return
    amount = input('Amount: ')
    result = bam.deposit(to_who, amount)
    if result['status'] == 'error':
        print(result['msg'])
    else:
        dm.set(accounts)
        name = bam.accounts[to_who]['name']
        print(f'{amount} $ deposited successfully to {name}!')

def withdraw():
    show_user_ids_and_balance()
    from_who = input('From who? (ID): ')
    if bam.accounts.get(from_who, {}).get('status', 'active') != 'active':
        print('Withdraw user is deactivated, operation not allowed.')
        return
    amount = input('Amount: ')
    result = bam.withdraw(from_who, amount)
    if result['status'] == 'error':
        print(result['msg'])
    else:
        dm.set(accounts)
        name = bam.accounts[from_who]['name']
        print(f"{amount} $ withdrawn from {name}!")

def deactivate():
    show_user_ids_and_balance()
    user_id = input('Enter user id to deactivate: ')
    result = bam.deactivate_user(user_id)
    if result['status'] == 'ok':
        dm.set(accounts)
        print(result['msg'])
    else:
        print(result['msg'])

def main():
    while True:
        show_menu()
        command = input('Select from menu: ')
        if command == '1':
            bam.show_info()
        elif command == '2':
            add_user()
        elif command == '3':
            transfer()
        elif command == '4':
            deposit()
        elif command == '5':
            withdraw()
        elif command == '6':
            deactivate()
        elif command == '7':
            print('Thank you for using this app, GoodBye..')
            break
        else:
            print('Invalid choice, Please try again.')    

main()