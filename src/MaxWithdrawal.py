class MaxWithdrawal:
    def __init__(self, num_years, tolerance=0.1):
        self.__num_years = num_years
        self.__tolerance = tolerance
    
    def maximum_withdrawal(self, balance, rate):
        # Calculate initial high bound - maximum possible withdrawal (annuity formula)
        high = (balance * rate) / (1 - (1 + rate) ** (-self.__num_years))
        low = 0
        
        return self.__binary_search_withdrawal(balance, rate, low, high, self.__tolerance, self.__num_years)
      
    
    def __binary_search_withdrawal(self, balance, rate, low, high, tolerance, years):
        if (high - low) <= tolerance:
            return (low + high) / 2
        
        mid = (low + high) / 2
        final_balance = self.__simulate_retirement(balance, rate, mid, years)
        
        if final_balance >= 0:
            return self.__binary_search_withdrawal(balance, rate, mid, high, tolerance, years)
        else:
            return self.__binary_search_withdrawal(balance, rate, low, mid, tolerance, years)
          
    
    def __simulate_retirement(self, initial_balance, rate, withdrawal, years):
        current_balance = initial_balance
        
        for year in range(years):
            current_balance = current_balance - withdrawal
            current_balance = current_balance * (1 + rate)
            
        return current_balance
      
