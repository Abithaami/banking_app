''''
    elif choose == "4":
        acc_num = int(input("Enter your account number: "))
        if acc_num in accounts:
            print("Transaction History:")
            print(file.read("assignment.txt"))
            for entry in accounts[acc_num][2]:
                print(entry)
        else:
            print("Account not found.")

    elif choose == "5":
        print("Thank you! Exiting...")
        break

    else:
        print("Invalid choice. Please choose between 1-6.")
'''