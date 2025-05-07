import random

def auto_create_accunut():
    return random.randint(100000,999999)
    #print(f"your account number is:{acconut_number}")
    

def create_customer():
    name=input("Enter your name:")
    user_name=input("Enter your user name:")
    password=input("Enter your password:")
    account_num=auto_create_accunut()

    with open ("customer.txt","r+") as file:
        file.write(f"{name},{user_name},{password},{account_num}\n")

    print(f"Your account number is: {account_num}")
    return account_num



with open ("customer.txt","r") as file:
    lines=file.readlines()
    print(lines)

def deposite(account_num):
    acc=int(input("Enter your account number: "))
    if account_num == acc:
        print("ok") 
    else:
        print("not ok")


deposite(create_customer)