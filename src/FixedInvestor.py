from Data import data

class FixedInvestor:
    def __init__(self):
        self.principal = data.principal
        self.years = data.years
        self.rate = data.rate

    @classmethod
    # Simulates the compound growth of retirement savings over a fixed period of time and interest rate.
    def fixed_investor(cls, principal, years, rate):
        balance = principal * (1 + rate) ** years # Formula for compound interest 
        data.balance = balance
        return balance 