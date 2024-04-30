# Bank Account 🏦

🔽 class BankAccount:
🔽  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first name
        self.last_name = last name
        self.account_id = account id
        self.account_type = account type
        self.pin = pin
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance
        
    def display_balance(self):
        print(f"${self.balance}")
        
checking_account = BankAccount("Jane", "Doe", 13243546, "checking", 0000, 250.00)
checking_account.deposit(100)
checking_account.display_balance()
checking_account.withdraw(50)
checking_account.display_balance()