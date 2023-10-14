class User:
    Users = []
    def __init__(self,name,email,address,account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = self.email + '100'
        self.transaction_histories = []
        self.loan_limit = 2
        self.total_loan = 0
        self.is_bankrupt = True
        self.is_loan = True
        User.Users.append(self)

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            self.transaction_histories.append(f'Depositing {amount}')
            print(f'Deposited {amount}. New balance: {self.balance}\n')
        else:
            print('Invalid deposit amount\n')

    def withdrawal(self, amount):
        
        if amount >= 0 and amount <= self.balance:
            if is_bankrupt:
                self.balance -= amount
                self.transaction_histories.append(f'Withdrawing {amount}')
                print(f'Withdrew ${amount}. New balance: {self.balance}\n')
            else:
                print('Bank is bankrupt\n')
        else:
            print('Invalid withdrawal amount\n')
        

    def transfer_amount(self,account,amount):
        if amount >= 0 and amount <= self.balance:
            if account:
                self.balance -= amount
                account.balance += amount
                print(f"Transferred ${amount} to {account.name} successfully")
                self.transaction_histories.append(f"Transferred ${amount} to {account.name} successfully\n")
            else:
                print('This account is no exist\n')
        else:
            print('Invalid transfer amount\n')

    def check_balance(self):
        print(f'Your available balance: {self.balance}\n')
        
    def transaction_history(self):
        print('----------Transaction History----------')
        for i in self.transaction_histories:
            print(i)
        print('---------------------------------------')

    def take_loan(self,amount):
        if self.is_loan:
            if self.loan_limit <= 0:
                print('Loans cannot be taken\n')
            else:
                self.balance += amount
                self.loan_limit -= 1
                self.total_loan += amount
                self.transaction_histories.append(f"Loan origination {amount}")
                print(f'Successful loan : {amount}\n')
        else:
            print('Bank is bankrupt\n')

    def delete_account(self, account_number):
        for account in self.Users:
            if account.account_number == account_number:
                self.Users.remove(account)
                print(f"Account deleted successfully\n")

    def all_user_list(self):
        print('------------All Users List-----------')
        for account in self.Users:
            print(f'User name: {account.name}')
        print('')

    def total_available_balance(self):
        total = 0
        for account in self.Users:
            # print(account.balance)
            total += account.balance
        print(f'Total available balance: {total}\n')

    def total_loan_amount(self):
        total = 0
        for account in self.Users:
            # print(account.total_loan)
            total += account.total_loan
        print(f'Total loan amount: {total}\n')

    def on_of_loan(self,account_number,conditions):
        if conditions == 'on':
            # self.is_loan = True
            for account in self.Users:
                if account.account_number == account_number:
                    account.is_loan = True
                    print(f'Successfully account {account.account_number} is True\n')
        elif conditions == 'off':
            for account in self.Users:
                if account.account_number == account_number:
                    account.is_loan = False
                    print(f'Successfully account {account.account_number} is False\n')
        else:
            print('Its on a valid condition\n')


current_user = None

while(True):
    print('1. User options: ')
    print('2. Admin options: ')
    print('3. Exit: ')
    print('************************')
    op = int(input('Enter chose option: '))
    if op == 1:
        print('1. Create account: ')
        print('2. Deposit: ')
        print('3. Withdraw: ')
        print('4. Show info: ')
        print('5. Transfer taka: ')
        print('6. Check available balance: ')
        print('7. Transaction history: ')
        print('8. Bank loan: ')
        print('************************')
        ch = int(input('Enter your choice: '))
        if ch == 1:
            name = input('Enter your name: ')
            email = input('Enter your email: ')
            address = input('Enter your address: ')
            account_type = input('Enter your account type: ')
            current_user = User(name,email,address,account_type)
            print(f'Account create successfully, Account Number: {current_user.account_number}\n')
            
        elif ch == 2:
            amount = int(input('Deposit amount: '))
            current_user.deposit(amount)

        elif ch == 3:
            amount = int(input('Withdraw amount: '))
            current_user.withdrawal(amount)

        elif ch == 4:
            print('---------------------')
            print(f' Account number: {current_user.account_number} \n My name: {current_user.name} \n My email: {current_user.email}\n My address: {current_user.address} \n Account type: {current_user.account_type} \n My balance: {current_user.balance} \n My loan: {current_user.total_loan} \n{current_user.is_bankrupt}')
            print('---------------------')

        elif ch == 5:
            accountNumber = input('Transfer account number: ')
            amount = int(input('Transfer amount: '))

            kkAcount = None
            for i in User.Users:
                if i.account_number == accountNumber:
                    kkAcount = i
                    break
            else:
                print('Account does not exist')
            
            if kkAcount:
                current_user.transfer_amount(kkAcount,amount)

        elif ch == 6:
            current_user.check_balance()
            
        elif ch == 7:
            current_user.transaction_history()

        elif ch == 8:
            taka = int(input('Enter loan amount: '))
            current_user.take_loan(taka)

    if op == 2:
        name = input('Please provide admin name: ')
        password = input('Enter the correct password: ')

        if name == 'admin' and password == '123':
            print('1. Create account: ')
            print('2. Delete any user account: ')
            print('3. See all user accounts list: ')
            print('4. Check the total available balance of the bank: ')
            print('5. Check the total loan amount: ')
            print('6. Can on or off the loan feature of the bank: ')
            print('************************')
            ts = int(input('Enter chose option: '))
            if ts == 1:
                name = input('Enter your name: ')
                email = input('Enter your email: ')
                address = input('Enter your address: ')
                account_type = input('Enter your account type: ')
                current_user = User(name,email,address,account_type)
                print(f'Account create successfully, Account Number: {current_user.account_number}\n')
            elif ts == 2:
                accountNumber = input('Enter account number: ')
                current_user.delete_account(accountNumber)
            elif ts == 3:
                current_user.all_user_list()
            elif ts == 4:
                current_user.total_available_balance()
            elif ts == 5:
                current_user.total_loan_amount()
            elif ts == 6:
                accountNumber = input('Enter account number: ')
                on_of = input('If you want to activate the loan, turn it on or off: ')
                current_user.on_of_loan(accountNumber,on_of)
        else:
            print('You are not an admin')

    elif op== 3:
        break
            
