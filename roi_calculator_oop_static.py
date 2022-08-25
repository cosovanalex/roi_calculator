class RoiCalculator:
    @staticmethod
    def cash_flow(income,expenses, investments):
        x = income
        y = expenses
        z = investments
        a = x - y
        return ((12 * a) / z) * 100


p1 = RoiCalculator()
print(f"Your Cash on Cash ROI is: {RoiCalculator.cash_flow(2000, 1610, 50000)}%")

p2 = RoiCalculator()
print(f"Your Cash on Cash ROI is: {RoiCalculator.cash_flow(500, 230, 10000)}%")


        
            
    
    
    
    
    