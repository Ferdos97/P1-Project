from datetime import datetime as dt

class BankAccountManagement:
    def __init__(self, accounts:dict):
        self.accounts = accounts
        
    def show_info(self):
        if not self.accounts:
            print("No data to show!")
            return
        
        for id in self.accounts:
            print(f"{id}- {self.accounts[id]['name']} ({self.accounts[id]['balance']})")
   
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
        if from_who not in self.accounts:
            return {'status': 'error', 'msg': 'Withdraw user does not exist!'}
        if to_whom not in self.accounts:
            return {'status': 'error', 'msg': 'Deposit user does not exist!'}
        if self.accounts[from_who]['balance'] < amount:
            return {'status': 'error', 'msg': 'Withdraw user does not have enough balance!'}
           
        try: 
            self.accounts[from_who]['balance'] -= amount
            self.accounts[to_whom]['balance'] += amount
            
            self.accounts[from_who]['history'].append(
                {'time': dt.now().strftime('%Y-%m-%d %H:%M'), 'type': 'withdraw', 'amount': amount}
            )

            self.accounts[to_whom]['history'].append(
                {'time': dt.now().strftime('%Y-%m-%d %H:%M'), 'type': 'deposite', 'amount': amount}
            )
            return {'status': 'ok'}
            
        except:
            return {'status': 'error', 'msg': 'Some error happend..'}
    

    def deposit(self, to_who:str, amount):
        try:
            to_who = int(to_who)
            amount = float(amount)
        except:
            return {'status': 'error', 'msg': 'Invalid input: Please provide valid numeric values for IDs and amount.'}
        
        to_who = str(to_who)
        if to_who not in self.accounts:
            return {'status': 'error', 'msg': 'Account not found!'}
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
