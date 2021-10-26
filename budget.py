import math

class Category:
    
    # class attribute 
    
    
    def __init__(self, budget_category):
        self.budget_category = budget_category
        self.ledger = []
    
    def __repr__(self):
        s = f"{self.budget_category:*^30}\n" 
        acc = 0
        
        for item in self.ledger:
            print("The item: ", item)
            s += f"{item['description']}{item['amount']:>{30-len(item['description'])}}\n"
            acc += item['amount']
            
        s += f"Total: {acc}"
        return s
    """"""
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
"""
food = Category("Food")
entertainment = Category("Entertainment")
food.deposit(100,"Pizza Party")
food.transfer(25, entertainment)
print(str(food))

print(entertainment.ledger)

print(food.ledger)

print(food.get_balance())
print(entertainment.get_balance())
"""
def create_spend_chart(categories):
    dictionary = calculate_percentages(categories)
    create_strings(dictionary)
    
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

        number = int((dictionary[i]/total_withdrawals) * 100)
        dictionary[i] = round_down(number)
        
    return dictionary
    
def create_strings(dictionary):
    position_counter_1 = 4
    bottom_line = "    _"
    all_strings = {100:"100|            ", 90: " 90|            ",80: " 80|            ",70:" 70|            ",
                   60:" 60|            ", 50: " 50|            ",40:" 40|            ",30:" 30|            ",
                   20:" 20|            ", 10:" 10|            ",0:"  0|            "}
    list_ = []
    
    #Bar chart
    for i in dictionary:
        percentage = dictionary[i] 
        
        position_counter_1 += 3
        while percentage >= 0:
            string = all_strings[percentage] 
            all_strings[percentage] = replace_string(string, position_counter_1, 'o')
            percentage -= 10
        tuple_ = (i, position_counter_1)
        list_.append(tuple_)

    for i in all_strings:
        print(all_strings[i])
        
    #Closing line
    if len(dictionary) > 0:
        for i in range(len(dictionary)):
            if i == 0:
                bottom_line += '_'
            else:
                bottom_line += '___'
        
        bottom_line += '__'
    else:
        bottom_line = ''
        
    print(bottom_line)
        
    #Category Names
    previous = ''
    longest_name = ''
    for i in dictionary:
        if len(str(i)) > len(previous):
            longest_name = i 
        else:
            longest_name = previous
    string = "               "
    #Creating vertical strings
    rtn_string = ""
    replace_str = "               "
    for i in range(0, len(longest_name)):
        replace_str = "               "
        for j in list_:
            
            if i < len(j[0]):
                replace_str = replace_string(replace_str, j[1], j[0][i])
            else:
                replace_str = replace_string(replace_str, j[1],' ')
            """
                rtn_string += replace_string(string, j[1], j[0][i])
            else:
                rtn_string += replace_string(string, j[1], ' ')
            """
            #print(replace_str)
        
        replace_str += "\n"
        rtn_string += replace_str
        
    
    print(rtn_string) 
           
def round_down(percentage):
    if percentage >= 0 and percentage < 10:
        return 0
    elif percentage >= 10 and percentage < 20:
        return 10
    elif percentage >= 20 and percentage < 30:
        return 20
    elif percentage >= 30 and percentage < 40:
        return 30
    elif percentage >= 40 and percentage < 50:
        return 40
    elif percentage >= 50 and percentage < 60:
        return 50
    elif percentage >= 60 and percentage < 70:
        return 60
    elif percentage >= 70 and percentage < 80:
        return 70
    elif percentage >= 80 and percentage < 90:
        return 80
    elif percentage >= 90 and percentage < 100:
        return 90
    elif percentage == 100:
        return 100
    

        
def replace_string(string, replace_position, char):
    new_list = []
    for i in range(0, len(string)):
        new_list.append(string[i])
    """ 
    print("----------------------------------------------")
    print(string, " ",replace_position,"   ---  ", new_list)
    print("----------------------------------------------")
    """
    new_list[replace_position] = char
    new_string = ''.join(new_list)
    
    return new_string

#create_spend_chart([food, entertainment])