class Category:
    
    # class attribute 
    ledger = []
    
    def __init__(self, budget_category):
        self.budget_category = budget_category

    def deposit(self, amount, description):        
        self.ledger.append({"amount": amount, "description": description})
        
    
    def withdraw(self, amount, description):
        self.ledger.append({"amount": -amount, "description": description})

    
    def transfer(self, amount, budget_category):
        self.withdraw("Transfer to "+budget_category)
        
        
    
    def check_funds(self):
        pass
    
    def create_spend_chart(categories):
        pass