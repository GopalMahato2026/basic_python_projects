def main():
    main_balance = 0  # This variable keeps track of balance

    def deposit():
        try:    
            user_money = float(input("Amount to deposit: "))
            if user_money < 0:
                print("Deposited amount can't be negative!")
                return 0
            else:
                print(f"{user_money}/- deposited successfully!")
                return user_money
        except ValueError:
            print("Enter a valid amount")
            return 0

    def withdraw():
        try:    
            user_withdraw = float(input("Amount to Withdraw: "))
            if user_withdraw < 0:
                print("Withdrawal amount can't be negative!")
                return 0
            return user_withdraw        
        except ValueError:
            print("Please enter a valid withdraw amount!")
            return 0

    def check_balance():
        print(f"Total Balance: {main_balance}/-")
        
    while True:
        print("\nSimple Banking Program")
        print("1. Deposit Money\n2. Withdraw Money\n3. Check Balance\n4. Exit")
        try:
            main_user = int(input("Enter your choice: "))
            if main_user not in [1, 2, 3, 4]:
                print(f"{main_user} is not a valid choice!")
                continue
        except ValueError:
            print("Enter a valid choice!")
            continue

        if main_user == 1:
            main_balance += deposit()

        elif main_user == 2:
            amount = withdraw()
            if amount <= 0:
                continue
            if amount > main_balance:
                print("Insufficient funds!")
            else:
                main_balance -= amount
                print(f"{amount}/- withdrawn successfully!")

        elif main_user == 3:
            check_balance()

        elif main_user == 4:
            print("Have a Nice Day!")
            break        

if __name__ == "__main__":
    main()
