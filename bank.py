
print("***********************BANK MANAGEMENT PROJECT***********************")
class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 10000

    def get_balance(self):
        return self.balance
    def withdraw (self , amount):
        if amount < self.min_withdraw:
            return f"no money for you. Minimum need to take {self.min_withdraw} taka"
        elif amount > self.max_withdraw:
            return f"crosses max limit : {self.max_withdraw}"
        elif amount > self.balance:
            return "No money sorry"
        else:
            self.balance = self.balance -amount
            return f"Here is yuor money : {amount}"
    def deposit(self, amount):
        self.balance = self.balance + amount

print("Enter amount: ")
my_bank = Bank(int(input()))
def menu():
        
        print("[1] Balance")
        print("[2] Withdraw")
        print("[3] Deposite money")

menu()
option=int(input("enter ur option: ")) 



while option !=0:
    if option == 1:
        print("Your current balance: ")
        print(my_bank.get_balance())
       
    
    elif option == 2:
        print("How much money do you want to withdraw?: ")
        reply = my_bank.withdraw(int(input()))
        print(reply)
        

    elif option == 3:
        print("How much money do you want to deposite?: ")
        my_bank.deposit(int(input()))
        print(my_bank.get_balance())
        
    
    else:
        print("Invalid option")
        
    
    print()
    menu()
    option=int(input("enter ur option: ")) 
    









