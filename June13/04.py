from random import randint

class Credit_cards:
    bank = " "
    kind = " "
    number = 0
    balance = 0
    limits = 0
    
    def __init__(self, bank, kind, number = 0):
        self.bank = bank
        self.kind = kind
        self.number = randint(4000000000000000, 4999999999999999)

    
    def __repr__(self) -> str:
        msg = "Credit card of the Bank: %s, type/kind: %s, number: %d " % (self.bank, self.kind, self.number)
        return msg 
    
    def show_replenishment_of_balance(self, balance = 0):
        print(self.number)
        self.balance += int(input("Enter the amount to replenish:$ "))
        print("Your balance:$ %d" % self.balance)
        
    def get_transaction(self, balance = 0):
        print(self.number)
        transfer = int(input("Enter the amout you want to trasfer:$ "))
        if transfer <= self.balance:
            print("Transaction completed successfully.")
            result = self.balance - transfer
            print("Your balance is: $ %d" % result)
        else:
            print("Please replenish your balance first.")
            
    def pay(self, balance = 0):
        print(self.number)
        payment_amount = int(input("Amount for payment is: $ "))
        if payment_amount <= self.balance:
            print("Payed.")
            result = self.balance - payment_amount
            print("Yourbalance is: %d" % result)
        else:
            print("Don't have enougth balance to pay!")
            
    def convert(self, balance = 0):
        print(self.number)
        amount = int(input("Enter the amount for conversation to 'tenge': $ "))
        result = amount * 450
        if amount <= self.balance:
            print("Converted $ %d to %d tenge" % (amount, result))
        else:
            print("Not enought balance!")                   
        
        
hcb = Credit_cards("Home Cradit Bank", "Visa")
hcb.show_replenishment_of_balance()
hcb.pay()
print(hcb)

kaspi = Credit_cards("Kapsi Bank", "Master card")
kaspi.show_replenishment_of_balance()
kaspi.convert()
print(kaspi)