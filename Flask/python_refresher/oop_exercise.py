class Account():
    
    def __init__(self , owner , balance):
        self.owner = owner
        self.balance = balance
        
    def deposit(self,amount):
        self.balance += amount
        print("deposit successful")
    
    def withdraw(self,amount):
        balance = self.balance
        if balance > amount :
            balance -= amount
            print('withdrawl successful')
        else :
            print('withdrawl failed')

    
account1 = Account("Billy" , 1000)
account1.deposit(100)
account1.withdraw(5000)
print(account1.balance)