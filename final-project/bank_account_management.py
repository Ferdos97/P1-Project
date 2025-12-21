from datetime import datetime as dt

class BankAccountManagement:
    def __init__(self, accounts:dict):
        self.accounts = accounts

    def show_info(self):
        if not self.accounts:
            print("No data to show!")
            return
        for id in self.accounts:
            status = self.accounts[id].get('status', 'active')
            name = self.accounts[id]['name']
            balance = self.accounts[id]['balance']
            status_display = f"({status.capitalize()})" if status != 'active' else ""
            print(f"{id}- {name} {status_display} ({balance})")
            for history in self.accounts[id]['history']:
                print(f'\t- {history.get("type")} {history.get("amount")} at {history.get("time")}')

    def add_user(self, name:str, first_amount:float):
        if not name:
            return {'status': 'error', 'msg': 'Name can not be empty!'}
        if not name.isalpha():
            return {'status': 'error', 'msg': 'Name must contain only letters!'}
        try:
            first_amount = float(first_amount)
        except:
            return {'status': 'error', 'msg': 'Amount should be a number!'}
        id = len(self.accounts) + 1
        self.accounts.update({
            str(id): {
                    'name': name, 
                    'balance': first_amount, 
                    'history': [
                        {'time': dt.now().strftime('%Y-%m-%d %H:%M'), 'type': 'deposit', 'amount': first_amount},
                    ],
                    'status': 'active'     
                }
        })
        return {'status': 'ok'}

    def transfer(self, from_who:str, to_whom:str, amount:str): 
        try:
            from_who = int(from_who)
            to_whom = int(to_whom)
            amount = float(amount)
        except:
            return {'status': 'error', 'msg': 'Invalid input: Please provide valid numeric values for IDs and amount.'}          
        from_who = str(from_who)
        to_whom = str(to_whom)
        if from_who == to_whom:
            return {'status': 'error', 'msg': 'Transfer between the same account is not allowed.'}
        if from_who not in self.accounts:
            return {'status': 'error', 'msg': 'Withdraw user does not exist!'}
        if self.accounts[from_who].get('status', 'active') != 'active':
            return {'status': 'error', 'msg': 'Withdraw user is deactivated, operation not allowed.'}
        if to_whom not in self.accounts:
            return {'status': 'error', 'msg': 'Deposit user does not exist!'}
        if self.accounts[to_whom].get('status', 'active') != 'active':
            return {'status': 'error', 'msg': 'Deposit user is deactivated, operation not allowed.'}
        if self.accounts[from_who]['balance'] < amount:
            return {'status': 'error', 'msg': 'Withdraw user does not have enough balance!'}
        try: 
            self.accounts[from_who]['balance'] -= amount
            self.accounts[to_whom]['balance'] += amount
            
            self.accounts[from_who]['history'].append(
                {'time': dt.now().strftime('%Y-%m-%d %H:%M'), 'type': 'withdraw', 'amount': amount}
            )
            self.accounts[to_whom]['history'].append(
                {'time': dt.now().strftime('%Y-%m-%d %H:%M'), 'type': 'deposit', 'amount': amount}
            )
            return {'status': 'ok'}
        except:
            return {'status': 'error', 'msg': 'Some error happened..'}
        
    def can_transfer(self, from_who: str, to_whom: str) -> dict:
        try:
            from_who_int = int(from_who)
            to_whom_int = int(to_whom)
        except:
            return {'status': 'error', 'msg': 'Invalid user IDs.'}
        if from_who_int == to_whom_int:
            return {'status': 'error', 'msg': 'Transfer between the same account is not allowed.'}
        return {'status': 'ok'}

    def deposit(self, to_who:str, amount):
        try:
            to_who = int(to_who)
            amount = float(amount)
        except:
            return {'status': 'error', 'msg': 'Invalid input: Please provide valid numeric values for IDs and amount.'}
        to_who = str(to_who)
        if to_who not in self.accounts:
            return {'status': 'error', 'msg': 'Account not found!'}
        if self.accounts[to_who].get('status', 'active') != 'active':
            return {'status': 'error', 'msg': 'Deposit user is deactivated, operation not allowed.'}
        if amount <= 0:
            return {'status': 'error', 'msg': 'Amount must be positive.'}
        try:
            self.accounts[to_who]['balance'] += amount
            self.accounts[to_who]['history'].append({
                'time': dt.now().strftime('%Y-%m-%d %H:%M'),
                'type': 'deposit',
                'amount': amount
            })
            return {'status': 'ok'}
        except Exception as e:
            return {'status': 'error', 'msg': f'Some error happened!: {e}'}

    def withdraw(self, from_who:str, amount):
        try:
            from_who = int(from_who)
            amount = float(amount)
        except:
            return {'status': 'error', 'msg': 'Invalid input: Please provide valid numeric values for IDs and amount.'}  
        from_who = str(from_who)
        if from_who not in self.accounts:
            return {'status': 'error', 'msg': 'Account not found!'}
        if self.accounts[from_who].get('status', 'active') != 'active':
            return {'status': 'error', 'msg': 'Withdraw user is deactivated, operation not allowed.'}
        if amount <= 0:
            return {'status': 'error', 'msg': 'Amount must be positive.'}
        if self.accounts[from_who]['balance'] < amount:
            return {'status': 'error', 'msg': 'Insufficient balance!'}
        self.accounts[from_who]['balance'] -= amount
        self.accounts[from_who]['history'].append({
            'time': dt.now().strftime('%Y-%m-%d %H:%M'),
            'type': 'withdraw',
            'amount': amount
        })
        return {'status': 'ok'}

    def deactivate_user(self, user_id: str):
        if user_id not in self.accounts:
            return {'status': 'error', 'msg': 'User not found!'}
        if self.accounts[user_id]['status'] == 'deactivated':
            return {'status': 'error', 'msg': 'User is already deactivated.'}
        self.accounts[user_id]['status'] = 'deactivated'
        return {'status': 'ok', 'msg': f"User {self.accounts[user_id]['name']} deactivated successfully."}
    