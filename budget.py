class Category:
    
    # class attribute 
    
    
    def __init__(self, budget_category):
        self.budget_category = budget_category
        self.ledger = []
    
    def __repr__(self):
        string = "*************{self.budget_category}*************\n"
        for i in self.ledger:
            string += i["description"] + str(i["amount"])+"\n"
        print("Total: "+self.get_balance)
    
    def get_balance(self):
        accumulated_total = 0
        for i in self.ledger:
            accumulated_total += float(i["amount"])
        return accumulated_total
      
    def deposit(self, amount, description): 
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
        if self.get_balance() < amount:
            return False
        else:
            return True 
    
    def display(self):
        print("*************Food*************")
        for i in self.ledger:
            print(i["description"] + str(i["amount"])+"\n")
        print("Total: "+self.get_balance)

food = Category("Food")
entertainment = Category("Entertainment")
food.deposit(100,"Pizza Party")
food.transfer(25, entertainment)
print(entertainment.ledger)
print(food.ledger)

print(food.get_balance())
print(entertainment.get_balance())
""""""
def create_spend_chart(categories):
    calculate_percentages(categories)
    
def calculate_percentages(categories):
    
    total_withdrawals = 0
    dictionary = {}
    
    # Get total withdrawals 
    for i in categories:
        category_ledger = i.ledger
        total_category_withdrawals = 0
        
        for j in category_ledger:
            if j["amount"] < 0: total_category_withdrawals += j["amount"]
        
        dictionary[i.budget_category] = abs(total_category_withdrawals) 
        total_withdrawals += abs(total_category_withdrawals) 
        
    #Calculate Percenteges 
    for i in dictionary:
        dictionary[i] =  int((dictionary[i]/total_withdrawals) * 100)
    
    return dictionary
    

create_spend_chart([food, entertainment])