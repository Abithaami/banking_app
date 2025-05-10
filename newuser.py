admin_name = "abi"
a_password = "abi@123"

accounts = {}


print("=========Welcome MiniBanking==========")
print("\n")
while True:
    print("1. Login ADMIN")
    print("2. Login Customer")
    print("3. Exit")
    print("\n")
    choose = input("Choose the number (1-3): ")

#ADMIN................................
    if choose == "1":
        a_name = input("Enter your username   ")
        a_p_word = input("Enter your password   ")
        if admin_name ==a_name and a_p_word == a_password:
            print("Successfully Login")
            while True:
                print("1. Add Customer Details")
                print("2. Create Account")
                print("3. Deposit Money")
                print("4. Withdraw Money")
                print("5. Check Balance")
                print("6. Transaction History")
                print("7.Exit")
                choose = input("Choose the number(1-7)")

#Add Customer Details....................
                if choose == "1":
                    def get_next_user_number():
                        try:
                            with open('add_customer_details.txt', 'r') as f:
                                lines = f.readlines()
                                last_u_num = 0
                                
                                for line in reversed(lines):
                                    if line.startswith("Your u_num is:"):
                                        # Extract the numeric part after "u" and convert to an integer
                                        last_u_num = int(line.split(": ")[1].strip()[1:])
                                        break
                                
                                # Increment the number and format as u01, u02, etc.
                                u_num = f"u{last_u_num + 1:02d}"
                        
                        except FileNotFoundError:
                            # Start from u01 if the file does not exist
                            u_num = "u01"
                        
                        return u_num

                        with open('add_customer_details.txt', 'a') as f:
                            f.write(f"Your user number is: {u_num}\n")
                        return u_num


                    u_num = get_next_user_number()
                    firstname = input("Enter your firstname   ")
                    lastname = input("Enter your lastname   ")
                    address = input("Enter your address   ")
                    ID_NUM = int(input("Enter your NIC number   "))


                    file = open('add_customer_details.txt','a')
                    file.write(f"Your user number is: {u_num}\n")
                    file.write(f"Your firstname is: {firstname}""\n")
                    file.write(f"Your lastname is: {lastname}""\n")
                    file.write(f"Your address is: {address}""\n")
                    file.write(f"Your ID_NUM is: {ID_NUM}""\n")
                    file.write("\n")
                    file.close()

                    print("Successfully added")

#Create Account....................
                elif choose == "2":
                    def get_next_account_number():
                        try:
                            with open('create_account.txt', 'r') as f:
                            
                                lines = f.readlines()
                                
                                last_acc_num = 1000  
                                for line in reversed(lines):
                                    if line.startswith("Your acc_num is:"):
                                        
                                        last_acc_num = int(line.split(": ")[1].strip())
                                        break
                                acc_num = last_acc_num + 1
                        except FileNotFoundError:
                            acc_num = 1001  

                    
                        with open('create_account.txt', 'a') as f:
                            f.write(f"Your acc_num is: {acc_num}\n")
                        return acc_num

                    def get_next_user_number():
                        try:
                            with open('add_customer_details.txt', 'r') as f:
                                lines = f.readlines()
                                last_u_num = 0  
                                
                                for line in reversed(lines):
                                    if line.startswith("Your u_num is:"):
                                        last_u_num = int(line.split(": ")[1].strip()[1:])
                                        break
                                u_num = f"u{last_u_num + 1:02d}"
                                
                        except FileNotFoundError:
                            u_num = "u01"
                        return u_num
   
                        with open('add_customer_details.txt', 'a') as f:
                            f.write(f"Your user_num is: {u_num}\n")
                        return  u_num

                    u_num = get_next_user_number()
                    acc_num = get_next_account_number()
                    name = input("Enter your name: ")
                    balance = int(input("Enter your balance: "))
                    user_name = input("Enter user name: ")
                    password = input("Enter your password: ")


                    with open('create_account.txt', 'a') as file:
                        file.write(f"Your name is: {name}\n")
                        file.write(f"Your balance is: {balance}\n")
                        file.write("\n")

                    file = open('user.txt','a')
                    file.write(f"Your acc_num is: {acc_num}\n")
                    file.write(f"Your user_num is: {u_num}\n")
                    file.write(f"Your user_name is: {user_name}""\n")
                    file.write(f"Your password is: {password}""\n")
                    file.write("\n")
                    file.close()

#Deposit Money....................
                elif choose == "3":
                    acc_num = int(input("Enter your account number: "))
                    if acc_num in accounts:
                        amount = int(input("Enter deposit amount: "))
                        accounts[acc_num][1] += amount
                        accounts[acc_num][2].append(f"Deposited: {amount}")
                        print(f"Deposit successful. New balance: {accounts[acc_num][1]}")
                    else:
                        print("Account not found.")

                        



#Withdrawel Money....................
                elif choose == "4":
                    acc_num = int(input("Enter your account number: "))
                    if acc_num in accounts:
                        amount = int(input("Enter withdrawal amount: "))
                        if accounts[acc_num][1] >= amount:
                            accounts[acc_num][1] -= amount
                            accounts[acc_num][2].append(f"Withdrew: {amount}")
                            print(f"Withdrawal successful. New balance: {accounts[acc_num][1]}")
                        else:
                            print("Insufficient funds.")
                    else:
                        print("Account not found.")


                    
#Check Balance.................................
                elif choose == "5":
                    acc_num = int(input("Enter your account number: "))
                    if acc_num in accounts:
                        print(f"Your current balance is: {accounts[acc_num][1]}")
                    else:
                        print("Account not found.")

# Transaction History................................
                elif choose == "6":
                    print(".........")

# Exit................................
                elif choose == "7":
                    print("Thank you ! Exiting...")
                    break

                else:
                    print("Invalid numbers, choose[1-7]")

# .............................................................................................................................................
# .............................................................................................................................................
# .............................................................................................................................................

# CUSTOMER LOGIN ................................
    elif choose == "2":
        u_name = input("Enter your username   ")
        u_p_word = input("Enter your password   ")

        file = open('user.txt','r')
        if user_name == u_name and password == u_p_word:
            print("Successfully Login")
            while True:
                print("1. Deposit Money")
                print("2. Withdraw Money")
                print("3. Check Balance")
                print("4. Transaction History")
                print("5.Exit")
                choose = input("Choose the number(1-5)")

#Deposit Money....................
                if choose == "1":
                    acc_num = int(input("Enter your account number: "))
                    if acc_num in accounts:
                        amount = int(input("Enter deposit amount: "))
                        accounts[acc_num][1] += amount
                        accounts[acc_num][2].append(f"Deposited: {amount}")
                        print(f"Deposit successful. New balance: {accounts[acc_num][1]}")
                    else:
                        print("Account not found.")



#Withdrawel Money....................
                elif choose == "2":
                    acc_num = int(input("Enter your account number: "))
                    if acc_num in accounts:
                        amount = int(input("Enter withdrawal amount: "))
                        if accounts[acc_num][1] >= amount:
                            accounts[acc_num][1] -= amount
                            accounts[acc_num][2].append(f"Withdrew: {amount}")
                            print(f"Withdrawal successful. New balance: {accounts[acc_num][1]}")
                        else:
                            print("Insufficient funds.")
                    else:
                        print("Account not found.")


                    
#Check Balance.................................
                elif choose == "3":
                    acc_num = int(input("Enter your account number: "))
                    if acc_num in accounts:
                        print(f"Your current balance is: {accounts[acc_num][1]}")
                    else:
                        print("Account not found.")

# Transaction History................................
                elif choose == "4":
                    print("...........")

# Exit................................
                elif choose == "5":
                    print("Thank you ! Exiting...")
                    break

                else:
                    print("Invalid numbers, choose[1-5]")

# .............................................................................................................................................
# .............................................................................................................................................
# .............................................................................................................................................

    elif choose == "3":
        print("Thank you ! Exiting...")
        break

    else:
        print("Invalid numbers, choose[1-3]")




