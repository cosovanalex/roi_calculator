class RoiCalculator:
    def __init__(self, income, expenses, investments):
        self.income = income
        self.expenses = expenses
        self.investments = investments
      

class Income():
    def __init__(self, rental_income=0, laundry=0, storage=0, misc=0):
        self.rental_income = rental_income
        self.laundry = laundry
        self.storage = storage
        self.misc = misc
    
    def total_income(self):
        self.rental_income = int(input("\nWhat is your monthly Rental Income? "))
        self.laundry = int(input("\nWhat is your monthly income from Laundry?(put 0 if it doesn't apply to you) "))
        self.storage = int(input("\nWhat is your monthly income from Storage?(put 0 if it doesn't apply to you) "))
        self.misc = int(input("\nWhat is your monthly income from other miscellaneous things related to the property?(put 0 if it doesn't apply to you) "))
        
        self.income = int(self.rental_income) + int(self.laundry) + int(self.storage) + int(self.misc)
        
        print(f"\nYour monthly income from this rental property is {self.income}$.")
        return self.income

class Expenses(RoiCalculator):
    def __init__(self, list_of_expenses):
        self.list_of_expenses = list_of_expenses
         
    def expenses(self):
        self.expenses = 0
        self.list_of_expenses = {
            "Tax" : int(input('\nHow much do you pay monthly for property tax? ')),
            "Insurance" : int(input('\nHow much do you pay monthly for property insurance? ')),
            'Utilities' : int(input('\nHow much do you pay monthly for Utilities? ')), 
            'HOA': int(input('\nHow much do you pay monthly for Home-Owner Association? ')), 
            'Lawn/Snow' : int(input('\nHow much do you pay monthly for lawn care/ snow removal? ')), 
            'Vacancy' : int(input('\nWhat are your monthly expenses with vacancy? ')), 
            'Repairs' : int(input('\nHow much do you pay monthly for property repairs? ')), 
            'CapEx' : int(input('\nHow much do you pay monthly for CapEx (renovations, maintenance, etc)? ')), 
            'Property Management' : int(input('\nWhat are your monthly fees for Property Management? ')),
            'Mortgage' : int(input('\nHow much do you pay monthly for mortgage? '))
            }
         
        for i in self.list_of_expenses.values():
            self.expenses = self.expenses + i
        
        print(f"\nYour total monthly expenses with this rental property are {self.expenses}$.")
        return self.expenses

class Investments(RoiCalculator):
    def __init__(self, total_investments):
        self.total_investments = total_investments
        
    def investments(self):        
        self.investments = 0
        self.total_investments = {
            "Down Payment" : int(input('\nHow much is your down payment? ')),
            'Closing Costs' : int(input('\nHow much are the closing costs? ')), 
            'Rehab Budget': int(input('\nWhat is your rehab budget? ')), 
            'Misc other' : int(input('\nDo you have any other miscellaneous costs not covered until now? '))
            }
        
        for i in self.total_investments.values():
            self.investments = self.investments + i

        print(f"\nYour total investments for this rental property are {self.investments}$.")
        return self.investments

class Calculator(RoiCalculator):
    def __init__(self, income, expenses, investments, cash_flow_final=0):
        super().__init__(income, expenses, investments)
        self.cash_flow_final= cash_flow_final

    def  __sub__(self, other):
        return self.income - self.expenses
        
    def cash_flow(self):
        self.CashFlow = (int(self.income) - int(self.expenses)) * 12
        print (f"\nYour Cash Flow is {self.CashFlow}")
        return self.CashFlow

    def roi(self):
        Roi = (int(self.CashFlow) / int(self.investments)) * 100
        print (f"\nYour Cash on Cash Return is {Roi}%")



p1 = Income()
p2 = Expenses([])
p3 = Investments([])
p4 = Calculator(p1.total_income(), p2.expenses(), p3.investments())
p4.cash_flow()
p4.roi()
