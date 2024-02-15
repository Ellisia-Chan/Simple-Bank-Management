import datetime

class BankAccount:
    def __init__(self, acc_id):
        self.id = acc_id
        self.acc_holder = {1: "John Doe", 2: "Olivia Anderson", 3: "Liam Patel", 4: "Sophia Gupta", 5: "Noah Sharma"}
        self.fixed_balance = {1: 1_000.00, 2: 500.00, 3: 1_000_000, 4: 10.00, 5: 3_000}
        self.current_balance = self.fixed_balance.get(self.id, 0.00)

    def account_holder(self):
        x = self.acc_holder.get(self.id)
        print("Account Holder: {}".format(x))

    def balance(self):
        print("Balance: ${}\n".format(self.current_balance))

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.current_balance:
                self.current_balance -= amount
                self.fixed_balance[self.id] = self.current_balance
                print("Withdrawal successful. Updated balance: ${}".format(self.current_balance))
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")

    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
            self.fixed_balance[self.id] = self.current_balance
            print("Deposit successful. Updated balance: ${}".format(self.current_balance))
        else:
            print("Invalid deposit amount.")

if __name__ == "__main__":
    while True:
        try:
            print("Date and Time:", datetime.datetime.now())
            acc_id = int(input("Account Number: "))
            
            if acc_id not in [1, 2, 3, 4, 5]:
                print("Account Number Not Found\n")
                continue
            
            account = BankAccount(acc_id)

            account.account_holder()
            account.balance()

            option = input("A) Withdraw \nB) Deposit \n> ").lower()

            if option == "a":
                withdrawal_amount = float(input("Withdrawal Amount: $"))
                account.withdraw(withdrawal_amount)
                break
            elif option == "b":
                deposit_amount = float(input("Deposit Amount: $"))
                account.deposit(deposit_amount)
                break
            else:
                print("Invalid option. Please enter 'A' or 'B'.")

        except ValueError:
            print("Invalid Input. Try Again")
            continue
