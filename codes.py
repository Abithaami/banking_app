import os

ADMIN_NAME = "abi"
ADMIN_PASSWORD = "abi@123"

DATA_DIR = "bank_data"
CUSTOMER_FILE = os.path.join(DATA_DIR, 'add_customer_details.txt')
ACCOUNT_FILE = os.path.join(DATA_DIR, 'create_account.txt')
USER_FILE = os.path.join(DATA_DIR, 'user.txt')
TRANSACTION_FILE = os.path.join(DATA_DIR, 'transaction_history.txt')

os.makedirs(DATA_DIR, exist_ok=True)


def get_next_user_number():
    try:
        with open(CUSTOMER_FILE, 'r') as f:
            lines = f.readlines()
            last_u_num = 0
            for line in reversed(lines):
                if line.startswith("Your user number is:"):
                    last_u_num = int(line.split(": ")[1].strip()[1:])
                    break
            return f"u{last_u_num + 1:02d}"
    except FileNotFoundError:
        return "u01"


def get_next_account_number():
    try:
        with open(ACCOUNT_FILE, 'r') as f:
            lines = f.readlines()
            last_acc_num = 1000
            for line in reversed(lines):
                if line.startswith("Your acc_num is:"):
                    last_acc_num = int(line.split(": ")[1].strip())
                    break
            return last_acc_num + 1
    except FileNotFoundError:
        return 1001


def add_customer_details():
    u_num = get_next_user_number()
    firstname = input("Enter your firstname: ")
    lastname = input("Enter your lastname: ")
    address = input("Enter your address: ")
    ID_NUM = input("Enter your NIC number: ")
    with open(CUSTOMER_FILE, 'a') as file:
        file.write(f"Your user number is: {u_num}\n")
        file.write(f"Your firstname is: {firstname}\n")
        file.write(f"Your lastname is: {lastname}\n")
        file.write(f"Your address is: {address}\n")
        file.write(f"Your ID_NUM is: {ID_NUM}\n")
        file.write("\n")
    print("Customer details added successfully.")


def create_account():
    acc_num = get_next_account_number()
    u_num = get_next_user_number()
    name = input("Enter your name: ")
    balance = int(input("Enter initial balance: "))
    user_name = input("Enter your username: ")
    password = input("Enter your password: ")
    with open(ACCOUNT_FILE, 'a') as file:
        file.write(f"Your acc_num is: {acc_num}\n")
        file.write(f"Your user_num is: {u_num}\n")
        file.write(f"Your name is: {name}\n")
        file.write(f"Your balance is: {balance}\n")
        file.write("\n")
    with open(USER_FILE, 'a') as file:
        file.write(f"Your acc_num is: {acc_num}\n")
        file.write(f"Your user_num is: {u_num}\n")
        file.write(f"Your user_name is: {user_name}\n")
        file.write(f"Your password is: {password}\n")
        file.write("\n")
    print("Account created successfully.")


def main():
    print("========= Welcome to MiniBanking =========")
    while True:
        print("\n1. Login as ADMIN")
        print("2. Login as Customer")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()
        if choice == "1":
            a_name = input("Enter your admin username: ").strip()
            a_password = input("Enter your admin password: ").strip()
            if a_name == ADMIN_NAME and a_password == ADMIN_PASSWORD:
                print("Successfully logged in as ADMIN.")
                while True:
                    print("\n1. Add Customer Details")
                    print("2. Create Account")
                    print("3. Exit")
                    admin_choice = input("Choose an option (1-3): ").strip()
                    if admin_choice == "1":
                        add_customer_details()
                    elif admin_choice == "2":
                        create_account()
                    elif admin_choice == "3":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid option. Please try again.")
            else:
                print("Invalid admin credentials. Please try again.")
        elif choice == "2":
            print("Customer login feature coming soon...")
        elif choice == "3":
            print("Thank you for using MiniBanking. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
