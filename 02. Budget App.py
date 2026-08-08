class Category:
    def __init__ (self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = ""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False
    
    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item['amount']
        return total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def __str__(self):
        output = self.name.center(30, '*') + '\n'
        for item in self.ledger:
            desc = item['description'][:23].ljust(23)
            amt = f"{item['amount']:.2f}".rjust(7)
            output += f"{desc}{amt}\n"
        output += f"Total: {self.get_balance():.2f}"
        return output

def create_spend_chart(categories):
    withdraw = []
    for cat in categories:
        cat_spent = 0
        for item in cat.ledger:
            if item['amount'] < 0:
                cat_spent += -item['amount']
        withdraw.append(cat_spent)
    total_spent = sum(withdraw)
    percentage = []
    for spent in withdraw:
        if total_spent == 0:
            percent = 0
        else:
            percent = int((spent / total_spent) * 100) // 10 * 10
        percentage.append(percent)
    
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{str(i).rjust(3)}| "
        for percent in percentage:
            if percent >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    names = [i.name for i in categories]
    max_len = max(len(name) for name in names)
    for i in range (max_len):
        chart += '    '
        for name in names:
            if i < len(name):
                chart +=f" {name[i]} "
            else:
                chart += '   '
        chart += ' '
        if i < max_len - 1:
            chart += "\n"
    return chart
    
#Test
if __name__ == "__main__":
    food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")

    clothing = Category("Clothing")
    food.transfer(50, clothing)
    clothing.withdraw(25.55, "shoes")

    auto = Category("Auto")
    auto.deposit(1000, "initial deposit")
    auto.withdraw(15, "gas")

    print(food)

    print(create_spend_chart([food, clothing, auto]))
