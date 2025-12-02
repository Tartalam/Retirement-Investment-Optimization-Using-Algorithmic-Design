class RetirementSimulator:
    
    def __init__(self, balance, expense, rate):
        self._initial_balance = balance
        self._balance = 0
        self._expense = expense
        self._rate = rate
        self._years = 0

    def simulate(self):
        years = 0
        current = self._initial_balance
    
        while current > 0:
            # WITHDRAW at beginning of year (to live on)
            current -= self._expense
        
            # If depleted, stop
            if current <= 0:
                break
            
            # Then earn returns on remaining balance
            current *= (1 + self._rate)
        
            years += 1
            if years > 200:
                return float('inf')
    
        self._years = years
        self._balance = current  # Update final balance
        return years