# file=open("Admin login datails.txt")
# file.write(username=("admin"))
# file.write(password=("admin#135"))
# file.close()

#Account= {}
def account_careation() :
    import random
    acconut_number=random.randint(100000,999999)
    print(f"Your new account number is:{acconut_number} ")
    acc_number=input("Enter your account number that you resive:")
    name=input("Enter your name:")
    address=input("Enter your address:")
    balance=float(input("Enter your balance:"))
    # print(f"Your account number is:",{acc_number})
    # print(f"Your name is:",{name})
    # print(f"Your password is:",{password})
    # print(f"Your address is:",{address})
    # Acount={acconut_number:{f"Account number":{acc_number},"Name":{name},"Balance":{balance},"Address":{address}}}
    # print(Account)
    account=acconut_number.get(acc_number)
    if not account:
        print("account not found")
        return
    
    with open("costomer.txt","a") as file:
        file.write(f"{acc_number},{name},{address},{balance}")
        print(file.read())

    


def requirements():
    print("------------------")
    print("MAIN MANU:")
    print("------------------")
    print("1.Account creation")
    print("2.Deposit money") 
    print("3.Withdraw money")
    print("4.Check balance")
    print("5.Transaction history")
    print("6.Exit")


#================= DEPOSITE MONEY =====================
def deposite() :
    global account_number
    acc_number=int(input("Enter your account number:"))
    account=acconut_number.get(acc_number)
    if not account:
        print("account not found")
        return
    try:
        dep_amount=int(input("Enter your deposite money:"))
        balance=balance+dep_amount
        print(f"New balance is:{balance}")
    except ValueError:
        print("Enter number only!")



#================= WITHDRAWAL MONEY =====================    
def withdraw() :
    try:
        global balance
        wit_amount=int(input("Enter your witdrawwal ammount:"))
        if wit_amount>0 and wit_amount<balance:
            balance=balance-wit_amount
            print("successfully withdrawal.")
            print(f"your account balance is:{balance}")
        else:
            print("your account balance is low")
    except ValueError:
        print("Enter numbers only only!")


#================= CHECK BALANCE =====================
def checkbalance():
    global balance
    print(f"Your account balance is:{balance}")


#================= EXIT =====================
def exit():
    print("THANK YOU")

def mainmanu():
    while True:
        requirements()
        option=int(input("Enter your option:(1,2,3,4,5,6):"))
        if option==1:
            account_creation()
        elif option==2:
            deposite()
        elif option==3:
            withdraw()
        elif option==4:
            checkbalance()
        else:
            exit()
            break


        

        



    



      
