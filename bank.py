import random
#====================== AUTO ACCONUT CREATION ============================

def auto_create_accunut():
    return random.randint(100000,999999)
#test command for git 
#===================== CREATE CUSTOMER (ACCOUNT CREATION) ===================================    

def create_customer():
    name=input("Enter your name:")
    user_name=input("Enter your user name:")
    password=input("Enter your password:")
    account_num=auto_create_accunut()
    balance=float(input("Enter you balance:"))

    with open ("customer.txt","a") as file:
        file.write(f"{name},{user_name},{password},{account_num},{balance},\n")

    print(f"Your account number is: {account_num}")
    print("DONT FORGOT YOUR ACCOUNT NUMBER!!")
    return account_num


#==================== DEPOSITE MONEY FUNCTION ===================================

def deposite():
    acc=input("Enter your account number:")
    pass_word=input("Enter your password:")
    with open ("customer.txt","r") as file:
        lines=file.readlines()
        
        for i in range(len(lines)):
            line_list=lines[i].split(",")
            if acc==line_list[3] and pass_word==line_list[2]:
                dep_amount=float(input("Enter your deposite amount: "))
                balance=float(line_list[4])
                balance+=dep_amount
                lines[i]=f"{line_list[0]},{line_list[1]},{line_list[2]},{line_list[3]},{balance},\n"
                log_transaction(acc,"Deposit",dep_amount,balance)
                print(f"your account balance is:{balance}")

                
        with open ("customer.txt","w") as file:  
            file.writelines(lines) 

         
#=================== WITHDRAW MONEY FUNCTION ====================================
def withdraw():
    acc = input("Enter your account number: ")
    pass_word = input("Enter your password: ")
    with open("customer.txt", "r") as file:
        lines = file.readlines()
    account_found = False  # Flag to track if the account was found
    for i in range(len(lines)):
        line_list = lines[i].split(",")
        if acc == line_list[3] and pass_word == line_list[2]:
            account_found = True
            wit_amount = float(input("Enter your withdrawal amount: "))
            balance = float(line_list[4])
            if wit_amount > 0 and wit_amount <= balance:# Check if withdrawal amount is valid
                balance -= wit_amount
                print(f"Withdrawal successful. Your account balance is: {balance}")
                lines[i] = f"{line_list[0]},{line_list[1]},{line_list[2]},{line_list[3]},{balance},\n"  # Rewrite the line
                log_transaction(acc, "Withdraw", wit_amount, balance)
            else:
                print("Check withdrawal amount! It should be less than or equal to your current balance.")
            break   # Exit the loop once account is found and processed
    else:
        print("Incorrect account number or password.")  # This will be executed if no account was found
    if account_found: # Rewrite the file
        with open("customer.txt", "w") as file:
            file.writelines(lines)


#================== CHECK BALANCE FUNCTION==========================================

def check_balance():
    acc=input("Enter your account number: ")
    pass_word=input("Enter your password:")
    with open ("customer.txt","r") as file:
        lines=file.readlines()
        for i in range(len(lines)):
            line_list=lines[i].strip().split(",")
            if acc==line_list[3] and pass_word==line_list[2]:
                print(f"Your account balance is :{line_list[4]}")
            else:
                print("check account number or password!")

#==================== TRANSACTION FUNCTION ==================================

def log_transaction(account_num, transaction_type, amount, balance):
    with open("transactions.txt", "a") as transaction_file:
        transaction_file.write(f"{account_num},{transaction_type},{amount},{balance},\n")

#==================== TRANSACTION HISTORY FUNCTION ===================================
def transaction_history():
    acc = input("Enter your account number: ")
    found = False
    try:
        with open("transactions.txt", "r") as transaction_file:
            lines = transaction_file.readlines()
            for line in lines:
                line_list = line.strip().split(",")
                if acc == line_list[0]:
                    print(f"transaction method: {line_list[1]}, Amount: {line_list[2]}, Balance: {line_list[3]}")
                    found = True  # account in this account the found varible chance true
        if not found:
            print("No transactions found for this account.")
    except FileNotFoundError:
        print("Transaction file not found.")

#===================== MAIN MENU FUNCTION =================================
def requirements():
    print("\n--------------------------------------------------")
    print("------------ WELCOME TO OUR BANK -----------------")
    print("--------------------------------------------------")
    print("--------------<<< MAIN MANU >>>-------------------")
    print("--------------------------------------------------\n")
    print("1.Account creation")
    print("2.Deposit money") 
    print("3.Withdraw money")
    print("4.Check balance")
    print("5.Transaction history")
    print("6.Exit")

#==================== CALLING FUNCTION ====================================
while True:
    requirements()
    try:
        option=int(input("Enter your option:(1,2,3,4,5,6):-"))
        if option==1:
            create_customer()
        elif option==2:
            deposite()
        elif option==3:
            withdraw()
        elif option==4:
            check_balance()
        elif option==5:
            transaction_history()
        elif option==6:
            print("----THANK YOU COME AGIN---")
            break
        else:
            print("Please enter a valid option (1-6).")
    except ValueError:
        print("Invalid input. Please enter a number.")       


    