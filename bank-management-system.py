import pickle
import os
import pathlib


class Account:
    account_no = 0
    account_holder_name = ""
    deposit_amount = 0
    account_type = ''

    def create_account(self):
        self.account_no = int(input("Enter account number: "))
        self.account_holder_name = input("Enter account holder name: ")
        self.account_type = input("Enter account type [C/S]: ")
        self.deposit_amount = int(input(
            "Enter initial deposit amount (>= 500 for saving account and >= 1000 for current account): "))

        print("\n\nAccount is created successfully")

    def show_account(self):
        print(f"Account number: {self.account_no}")
        print(f"Account holder name: {self.account_holder_name}")
        print(f"Type of account: {self.account_type}")
        print(f"Balance: {self.deposit_amount}")

    def modify_account(self):
        print(f"Account Number: {self.account_no}")

        self.account_holder_name = input("Modify account holder name: ")
        self.account_type = input("Modify account type:  ")
        self.deposit_amount = int(input("Modify Balance: "))

    def deposit_amount(self, amount):
        self.deposit_amount += amount

    def withdraw_amount(self, amount):
        self.deposit_amount -= amount

    def report(self):
        print(
            f"{self.account_no} {self.account_holder_name} {self.account_type}  {self.deposit_amount}")

    def get_account_no(self):
        return self.account_no

    def get_account_holder_name(self):
        return self.account_holder_name

    def get_account_type(self):
        return self.account_type

    def get_deposite_amount(self):
        return self.deposite_amount


def intro():
    print("\t\t\t\t*********************************")
    print("\t\t\t\tBANK MANAGEMENT SYSTEM")
    print("\t\t\t\t*********************************")

    input()


def write_account():
    account = Account()   # object is created here
    account.create_account()

    write_account_file(account)


def display_all():
    file = pathlib.Path("accounts.data")

    if file.exists():
        infile = open("accounts.data", "rb")
        mylist = pickle.load(infile)

        for item in mylist:
            print(
                f"{item.account_no} {item.account_holder_name} {item.account_type} {item.deposit_amount}")

        infile.close()
    else:
        print("No records found to display")


def display_specific_account(accountNumber):
    file = pathlib.Path("accounts.data")
    found = False
    if file.exists():
        infile = open("accounts.data", "rb")
        mylist = pickle.load(infile)

        infile.close()
        found = False

        for item in mylist:
            if item.account_no == accountNumber:
                print(f"You account Balance is: {item.deposit_amount}")
                found = True
    else:
        print("No records to search")

    if not found:
        print(f"{accountNumber} account number is not found in records")


def deposit_and_withdraw(accountNumber, option):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data", "rb")
        mylist = pickle.load(infile)
        infile.close()

        os.remove("accounts.data")

        for item in mylist:
            if item.account_no == accountNumber:
                if option == 1:
                    amount = int(input("Enter the amount to deposit: "))
                    item.deposit_amount += amount
                    print("You account is updated")
                elif option == 2:
                    amount = int(input("Enter the amount to withdraw: "))

                    if amount <= item.deposit_amount:
                        item.deposit_amount -= amount
                        print("You account is updated")
                    else:
                        print("You don't have enough money to withdraw")
    else:
        print("No records to search")

    outfile = open("newAccounts.data", "wb")
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename("newAccounts.data", "accounts.data")


def delete_account(accountNumber):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data", "rb")
        old_list = pickle.load(infile)
        infile.close()

        new_list = []
        for item in old_list:
            if item.account_no != accountNumber:
                new_list.append(item)

        print("Account deleted successfully")
        os.remove("accounts.data")

        outfile = open("newAccounts.data", "wb")
        pickle.dump(new_list, outfile)
        outfile.close()

        os.rename("newAccounts.data", "accounts.data")


def modify_account(accountNumber):
    file = pathlib.Path("accounts.data")

    if file.exists():
        infile = open("accounts.data", "rb")
        old_list = pickle.load(infile)
        infile.close()

        os.remove("accounts.data")

        for item in old_list:
            if item.account_no == accountNumber:
                item.account_holder_name = input(
                    "Enter the account holder name: ")
                item.account_type = input("Type the account type: ")
                item.despot_account = int(input("Enter the deposit amount: "))

        outfile = open("newAccounts.data",  "wb")
        pickle.dump(old_list, outfile)
        outfile.close()

        os.rename("newAccounts.data", "accounts.data")


def write_account_file(account):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data", "rb")
        old_list = pickle.load(infile)
        old_list.append(account)

        infile.close()
        os.remove("accounts.data")
    else:
        old_list = [account]

    outfile = open("newAccounts.data", "wb")
    pickle.dump(old_list, outfile)
    outfile.close()
    os.rename("newAccounts.data", "accounts.data")


def show_menu(menu):
    i = 0
    while i < len(menu):
        print(f"\t{i + 1} {menu[i]}")
        i += 1


# start of a program
option = 0
account = 0
intro()

while option != 8:
    print("\tMAIN MENU")

    menu_list = ["NEW ACCOUNT", "DEPOSIT AMOUNT", "WITHDRAW AMOUNT", "BALANCE ENQUIRY",
                 "ALL ACCOUNT HOLDER LIST", "CLOSE AN ACCOUNT", "MODIFY ACCOUNT", "EXIT"]
    show_menu(menu_list)

    option = int(input("Select Your option (1-8): "))

    if option == 1:
        write_account()
    elif option == 2:
        num = int(input("Enter your account number: "))
        deposit_and_withdraw(num, 1)
    elif option == 3:
        num = int(input("Enter your account number: "))
        deposit_and_withdraw(num, 2)
    elif option == 4:
        num = int(input("Enter your account number:"))
        display_specific_account(num)
    elif option == 5:
        display_all()
    elif option == 6:
        num = int(input("Enter your account number: "))
        delete_account(num)
    elif option == 7:
        num = int(input("Enter your account number: "))
        modify_account(num)
    elif option == 8:
        print("Thanks for using banking management system")
        break
    else:
        print("Invaid choice. Please choose correct option")

    ch = int(input("Enter you choice: "))
