class BudgetAdvisor:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, amount, category, type_):
        self.transactions.append({"amount": amount, "category": category, "type": type_})

    def total_income(self):
        return sum(t["amount"] for t in self.transactions if t["type"] == "income")

    def total_expense(self):
        return sum(t["amount"] for t in self.transactions if t["type"] == "expense")

    def category_spending(self):
        spending = {}
        for t in self.transactions:
            if t["type"] == "expense":
                spending[t["category"]] = spending.get(t["category"], 0) + t["amount"]
        return spending

    def generate_report(self):
        print("\nBudget Report:")
        print(f"Total Income: {self.total_income()}")
        print(f"Total Expenses: {self.total_expense()}")
        print(f"Net Savings: {self.total_income() - self.total_expense()}")
        print("Category-wise Spending:", self.category_spending())

# Example usage
advisor = BudgetAdvisor()
advisor.add_transaction(5000, "Salary", "income")
advisor.add_transaction(200, "Food", "expense")
advisor.add_transaction(300, "Transport", "expense")
advisor.add_transaction(100, "Entertainment", "expense")

advisor.generate_report()
