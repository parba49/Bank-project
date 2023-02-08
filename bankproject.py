print("***********************BANK MANAGEMENT PROJECT***********************")
class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 500
        self.max_withdraw = 15000
        
        
    
        

    def get_balance(self):
        return self.balance
    def withdraw (self , amount):
        if amount < self.min_withdraw:
            return f"Your request is less than minimum withdraw {self.min_withdraw} taka"
        elif amount > self.max_withdraw:
            return f"You don't take that money because of max_withdraw  {self.max_withdraw} taka"
        elif amount > self.balance:
            return "Sorry,not enough money"
        elif amount == self.balance:
            return "Done"
       
       
        else:
            self.balance = self.balance-amount
            return f"Here is your money :{self.balance}"
    def deposit(self, amount):
        self.balance = self.balance + amount
    
    


def menu():
        print("**Menu**")
        print("----------")
        print("----------")

        print("[1] Enter your amount: ")
        print("[2] Current balance")
        print("[3] Withdraw")
        print("[4] Deposite money")

menu()
option=int(input("enter ur option: ")) 



while option !=0:

    if option == 1:
        print("Enter amount: ")
        my_bank = Bank(int(input()))
       
    elif option == 2:
        print("Your current balance: ")
        print(my_bank.get_balance())
       
    
    elif option == 3:
        print("How much money do you want to withdraw?: ")
        reply = my_bank.withdraw(int(input()))
        print(reply)
        

    elif option == 4:
        print("How much money do you want to deposite?: ")
        my_bank.deposit(int(input()))
        print("Here is your money: ")
        print(my_bank.get_balance())
        
    
    else:
        print("Invalid option")
        
    
    print()
    menu()
    option=int(input("enter ur option: ")) 
    
