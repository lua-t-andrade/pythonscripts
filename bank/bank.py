# implementation of a bank system,
# OOP exercise

def value_not_num(): #for error handling purposes (never repeat yourself)
    print("Use only numbers. ")

class bank_account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit_money(self, amount):
        if amount < 0:
            print("You can't do that.")
        else:
            self.balance += amount
            print(f"New balance: {self.balance}")

    def withdraw_money(self, amount):
        if amount > self.balance:
            print("You don't have enough money for that.")
        else:
            self.balance -= amount
            print(f"New balance: {self.balance}")

    def check_balance(self):
        print(f"Your balance is {self.balance} right now.")

def bank_system():
    name = input("What is your name? ")
    new_account = bank_account(name, 0)
    
    #main loop
    while True:
        try:
            menu_input = int(input("What would you like to do today? (1) Deposit money (2) Withdraw money (3) Check your balance (4) Exit\n> "))
        except (ValueError, UnboundLocalError):
            value_not_num()
            break

        content = [str(new_account.name), str(new_account.balance)]

        def save_data(): #function to save account data, name and balance
            file = "newuser.txt"
            with open(file, "a+") as f:
                f.write("\n")
                f.write(str(content))
                f.write("\n")
                f.close()
        try:

            if menu_input == 1:
                amount = float(input("What amount to deposit? "))
                new_account.deposit_money(amount)
            if menu_input == 2:
                withdraw_amount = float(input("What amount to withdraw? "))
                new_account.withdraw_money(withdraw_amount)
            if menu_input == 3:
                new_account.check_balance()
            if menu_input == 4:
                save_data()
                break
        except ValueError:
            value_not_num()
            break

if __name__ == "__main__":
    bank_system()

