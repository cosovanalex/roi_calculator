
class RoiCalculator:
    def __init__(self, income, expenses, investments):
        self.income = income
        self.expenses = expenses
        self.investments = investments
        
    def cash_flow(self):
        a = self.income - self.expenses
        x = ((12 * a) / self.investments) * 100
        self.cash_flow = x
   
    def showRoi(self):
        print(f"Your Cash on Cash ROI is: {self.cash_flow}%")

p1 = RoiCalculator(2000, 1610, 50000)
p1.cash_flow()
p1.showRoi()


p2 = RoiCalculator(500, 230, 10000)
p2.cash_flow()
p2.showRoi()