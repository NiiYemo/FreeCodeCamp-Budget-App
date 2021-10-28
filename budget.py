"""
The Category class for budget allocations.
"""
class Category:
    """This Class instantiate's objects based on budget categories.

    The class is initialised with a budget category as a string. For the
    category, the class allows for deposits and withdrawals. Which are stored in a ledger
    as a list. The amount of money and a description of the transaction,
    are stored as a dictionary entry,
    within the ledger. Transfers can be made, the current balance can be viewed.
    Lastly a report of all transactions can be viewed from calling the string method and
    a chart of expendeture based on percentages.

      Typical usage example:

      food = budget.Category("Food")
      food.deposit(1000, "initial deposit")
      food.withdraw(10.15, "groceries")
      food.withdraw(15.89, "restaurant and more food for dessert")
    """
    def __init__(self, budget_category):
        self.budget_category = budget_category
        self.ledger = []

    def __str__(self):
        string = [self.budget_category.center(30, "*")]
        acc = 0
        for i in self.ledger:
            desc = i["description"][0:23]
            string.append("{:<23}{:>7.2f}".format(desc, i["amount"]))
            acc += i['amount']
        string.append("Total: {}".format(acc))
        return "\n".join(string)

    def get_balance(self):
        """Fetches the balance."""
        accumulated_total = 0
        for i in self.ledger:
            accumulated_total += float(i["amount"])
        return accumulated_total

    def deposit(self, amount, description = ""):
        """Adds an amount to the ledger.

        Args:
            amount: A double value.
            description: A string value, pertaining to the amount entered.
        """
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description = ""):
        """Adds an amount to from the ledger.

        Args:
            amount: A double value.
            description: A string value, pertaining to the amount entered.

        Returns:
            A boolean.
        """
        rtn = False
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            rtn = True
        return rtn

    def transfer(self, amount, destination_obj):
        """Withdraws an amount from the current object, then adds it to the
           destination object.

        Args:
            amount: A double value.
            destination_obj: Another Category object.

        Returns:
            A boolean is returned.
        """
        rtn = False
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + destination_obj.budget_category)
            destination_obj.deposit(amount, "Transfer from " + self.budget_category)
            rtn = True
        return rtn

    def check_funds(self, amount):
        """Returns a boolean, pertaining to whether an amount is more than
           the balance.

           Returns:
               A boolean is returned.
        """
        rtn = True
        if self.get_balance() < amount:
            rtn = False
        return rtn

    def spent(self):
        """Returns the expenditure from the category.

           Returns:
              A minus double number is returned. Which is calculated from the ledger.
        """
        expenditure = 0
        for i in self.ledger:
            amount = i["amount"]
            if amount < 0:
                expenditure += amount

        return -expenditure

def create_spend_chart(categories):
    """Returns a chart representation of the expenditure which is in percentages.

        Args:
            categories: A list of Category objects .

       Returns:
          A string is returned, formed from the calculted expenditures
          from the various categories within
          the list.
    """
    spending = [c.spent() for c in categories]
    total = sum(spending)
    percentages = [i * 100 / total for i in spending]
    string = ["Percentage spent by category"]
    for i in range(0, 11):
        level = 10 * (10 - i)
        single_line = '{:>3}| '.format(level)
        for j in percentages:
            if j >= level:
                single_line += "o  "
            else:
                single_line += "   "
        string.append(single_line)
    padding = " " * 4
    string.append(padding + "-" * 3 * len(spending) + "-")

    names = [c.budget_category for c in categories]
    max_name = max(map(len, names))
    for i in range(0, max_name):
        spaces_string = padding
        for name in names:
            spaces_string += " "
            spaces_string += name[i] if len(name) > i else " "
            spaces_string += " "

        string.append(spaces_string + " ")

    return "\n".join(string)
