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
    print('4- Deposite')
    print('5- Withdraw')
    print('6- Exit')
    print('\n')

def add_user():
    name = input('insert name: ')
    first_amount = input('insert amount: ')

    result = bam.add_user(name, first_amount)
    if result['status'] == 'ok':
        print(f"{name} is addedd successfully.")
    if result['status'] == 'error':
        print(result['msg'])    

def transfer():
    from_who = input('From who? (id): ')
    to_whom = input('To whom? (id): ')
    amount = input('Amount: ')
    
    result = bam.transfer(from_who, to_whom, amount)
    if result['status'] == 'error':
        print(result['msg'])
    else:
        from_name = bam.accounts[str(from_who)]['name']
        to_name = bam.accounts[str(to_whom)]['name']
        print(f"Successfully transferred {amount} $ from {from_name} to {to_name}.")

def deposit():
    to_who = input('To who? (id): ')
    amount = input('Amount: ')
    result = bam.deposit(to_who, amount)
    if result['status'] == 'error':
        print(result['msg'])
    else:
        name = bam.accounts[to_who]['name']
        print(f'{amount} $ deposited successfully to {name}!')

def withdraw():
    from_who = input('From who? (id): ')
    amount = input('Amount: ')
    result = bam.withdraw(from_who, amount)
    if result['status'] == 'error':
        print(result['msg'])
    else:
        name = bam.accounts[from_who]['name']
        print(f"{amount} $ withdrawn from {name}!")

def main():
    while True:
        show_menu()
        dm.set(accounts)
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
            print('Thank you for using this app, GoodBye..')
            break
        else:
            print('Invalid choice, Please try again.')    

main()