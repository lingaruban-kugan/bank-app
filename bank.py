import random

def auto_create_accunut():
    return random.randint(100000,999999)
    #print(f"your account number is:{acconut_number}")
    

def create_customer():
    name=input("Enter your name:")
    user_name=input("Enter your user name:")
    password=input("Enter your password:")
    account_num=auto_create_accunut()
    balance=float(input("Enter you balance:"))

    with open ("customer.txt","a") as file:
        file.write(f"{name},{user_name},{password},{account_num},{balance},\n")

    print(f"Your account number is: {account_num}")
    return account_num




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

         


def withdraw():
    acc=(input("Enter your account number: "))
    pass_word=input("Enter your password:")
    with open ("customer.txt","r") as file:
        lines=file.readlines()
        for i in range(len(lines)):
            line_list=lines[i].split(",")
            if acc==line_list[3] and pass_word==line_list[2]:
                wit_amount=float(input("Enter your withdrawal amount:"))
                balance=float(line_list[4])
                if wit_amount>0 and wit_amount<balance:
                    balance-=wit_amount
                    print(f"Withdraw success fully.your account balance is:{balance}")
                    lines[i]=f"{line_list[0]},{line_list[1]},{line_list[2]},{line_list[3]},{balance},\n"
                    log_transaction(acc,"Withdraw",wit_amount,balance)

                else:
                    print("Check withdrawal amount!")
            else:
                print("Enter correct account number and password!")
        with open ("customer.txt","w") as file:  
            file.writelines(lines) 


def check_balance():
    acc=int(input("Enter your account number: "))
    pass_word=input("Enter your password:")
    with open ("customer.txt","r") as file:
        lines=file.readlines()
        for i in range(len(lines)):
            line_list=lines[i].split(",")
            if acc==line_list[3] and pass_word==line_list[2]:
                print(f"Your account balance is :{line_list[4]}")


def log_transaction(account_num, transaction_type, amount, balance):
    with open("transactions.txt", "a") as transaction_file:
        transaction_file.write(f"{account_num},{transaction_type},{amount},{balance},\n")

def transaction_history():
    acc=int(input("Enter your account number: "))
    with open("transactions.txt", "a") as transactoin_file:
        lines=transactoin_file.readlines()
        for i in range(len(lines)):
            line_list=lines[i].split(",")
            if acc==line_list[0]:
                print(f"{line_list[1]},Amount is:{line_list[2]},Balance is:{line_list[3]}")


def requirements():
    print("------------ WELCOME TO OUR BANK -----------------")
    print("--------------------------------------------------")
    print("---<<< MAIN MANU >>>---")
    print("--------------------------------------------------")
    print("1.Account creation")
    print("2.Deposit money") 
    print("3.Withdraw money")
    print("4.Check balance")
    print("5.Transaction history")
    print("6.Exit")


while True:
    requirements()
    try:
        option=int(input("Enter your option:(1,2,3,4,5,6):"))
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


    