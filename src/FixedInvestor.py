class FixedInvestor:
    def __init__(self, principal, years, rate):
        self.principal = float(principal)
        self.years = int(years)
        self.rate = float(rate)

    @classmethod
    # Simulates the compound growth of retirement savings over a fixed period of time and interest rate.
    def fixed_investor(cls, principal, years, rate):
        return principal * (1 + rate) ** years # Formula for compound interest 