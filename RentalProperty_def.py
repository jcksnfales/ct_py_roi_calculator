class RentalProperty():
    """
        Defines a RentalProperty object.

        Attributes:
            investment - Total up-front cost from all expenses (down payment, closing cost, rehab expenses). NOT the total price of the unit. Expected to be an int.
            income - Total projected monthly profits from all income sources. Expected to be an int.
            expenses - Total projected monthly losses from all expenses. Expected to be an int.
    """
    def __init__(self, income, expenses, investment):
        self.income = income
        self.expenses = expenses
        self.investment = investment

    def calcROI(self):
        # since self.income and self.expenses are both monthly, we multiply by 12 to get the annual cash flow 
        cashFlow = 12 * (self.income - self.expenses)
        # then, divide annual cash flow by the total up-front investment 
        return float(cashFlow) / float(self.investment)