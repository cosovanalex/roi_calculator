class RoiCalculator:
    
    def __init__(self, income, expenses, investments):
        self.income = income
        self.expenses = expenses
        self.investments = investments
    @staticmethod    
    def roi_calc(CashFlow, investments):
        
        x = (int(CashFlow) / int(investments)) * 100
        print (f"\nYour Cash on Cash Return is {x}%")

income = int(input("\nWhat is your Total Monthly Income?\nThis includes things like:\n \tRental Income\n \tLaundry Income\n \tStorage Income\n \tMiscellanious Income the property brings in\nEnter amount: "))
expenses = int(input("\nWhat are your Total Monthly Expenses?\nThis includes things like:\n \tTaxes\n \tInsurance\n \tWater/sewer\n \tGarbage\n \tElectric\n \tGas\n \tHOA Fees\n \tLawn/Snow\n \tVacancy\n \tRepairs\n \tCapEx\n \tProperty Management\n \tMortgagen\nEnter amount: "))
investments = int(input("\nWhat is the total investment in the property?\nThis includes things like:\n \tDown Payment amount\n \tClosing Costs amount\n \tRehab Budget\n \tMisc Other\nEnter amount: "))
CashFlow = (income - expenses) * 12


p1 = RoiCalculator(income, expenses, investments)
p1.roi_calc(CashFlow, investments)



