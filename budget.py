class Category:
    
    # class attribute 
    ledger = []
    
    def __init__(self, budget_category):
        self.budget_category = budget_category
        
    def get_balance(self):
        accumulated_total = 0
        for i in self.ledger:
            accumulated_total += i["amount"]

        return accumulated_total
      
    def deposit(self, amount,   description): 
        self.ledger.append({"amount": amount, "description": description})
           
    def withdraw(self, amount, description):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else: 
            return False
        
    def transfer(self, amount, destination_obj):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + destination_obj.budget_category)
            destination_obj.deposit(amount, "Transfer from " + self.budget_category)
            return True
        else:
            return False
        
        
    def check_funds(self, amount):
        if self.get_balance() > amount:
            return False
        else:
            return True 
    
    def display(self):
        print("*************Food*************")
        for i in self.ledger:
            print(i["description"] + str(i["amount"])+"\n")
        print("Total: "+self.get_balance)
    
def create_spend_chart(self, categories):
    pass