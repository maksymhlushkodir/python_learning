class Account:
    def __init__(self, __owner: str, __balance: float = 0.0):
        self.__owner = __owner
        self.__balance = __balance

    def deposit(self, deposit_amount: float):
        if deposit_amount > 0.0:
            self.__balance += deposit_amount
            print(f'added to the account {deposit_amount}! Bank balance now {self.__balance}')

    def withdraw(self, withdraw_amount: float):
        if withdraw_amount > self.__balance:
            print('Insufficient funds error.')
        else:
            self.__balance -= withdraw_amount
            print(f'you withdraw funds in the amount of {withdraw_amount}. Bank balance now {self.__balance}')

    def get_balance(self):
        print(self.__balance)
        return self.__balance


class SavingsAccount(Account):
    def __init__(self, __owner: str, __balance: float = 0.0, interest_rate: float = 0.3):
        super().__init__(__owner, __balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        deposit = self.get_balance() * self.interest_rate
        self.deposit(deposit)
        print(f'Your deposit is {deposit}. Bank balance now {self.get_balance()}')


class Bank:
    def __init__(self, accounts: list=None):
        self.accounts = accounts
        if self.accounts is None:
            self.accounts = []

    def open_account(self, account: Account):
        self.accounts.append(account)

    def total_bank_balance(self):
        total = 0
        for account in self.accounts:
            total += account.get_balance()
        print(f'Total balance now {total}')

account1 = Account('', 100.0)
account2 = Account('', 100.0)

account1.deposit(100)
account2.withdraw(30)

savings = SavingsAccount('', 100.0)
savings.add_interest()

bank = Bank()

bank.open_account(account1)
bank.open_account(account2)

bank.total_bank_balance()