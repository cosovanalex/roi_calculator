Income = int(input("\nWhat is your Total Monthly Income?\nThis includes things like:\n \tRental Income\n \tLaundry Income\n \tStorage Income\n \tMiscellanious Income the property brings in\nEnter amount: "))
Expenses = int(input("\nWhat are your Total Monthly Expenses?\nThis includes things like:\n \tTaxes\n \tInsurance\n \tWater/sewer\n \tGarbage\n \tElectric\n \tGas\n \tHOA Fees\n \tLawn/Snow\n \tVacancy\n \tRepairs\n \tCapEx\n \tProperty Management\n \tMortgagen\nEnter amount: "))
Investments = int(input("\nWhat is the total investment in the property?\nThis includes things like:\n \tDown Payment amount\n \tClosing Costs amount\n \tRehab Budget\n \tMisc Other\nEnter amount: "))
def ROI(Income, Expenses, Investments):
    CashFlow = (Income - Expenses) * 12
    ROI = (CashFlow/Investments) * 100
    print (f"\nYour Cash on Cash Return is {ROI}%")

ROI(Income, Expenses, Investments)
