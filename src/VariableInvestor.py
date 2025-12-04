#Author: Raman Watson
#Date: 03/12/2025
#ID: 1701474
#Description: Calculates investment growth with variable interest rates over multiple periods
#Atrributions: AI was used to provide a more efficient algorithm, weeding out the unnecessary code I had.

class VariableInvestor:
    """Utility class for variable rate calculations."""
    
    @staticmethod
    def calculate(principal, rate_list):
        """Main calculation method."""
        if principal <= 0:
            raise ValueError("Principal must be positive")
        
        balance = principal
        for rate in rate_list:
            if rate <= -1:
                raise ValueError(f"Rate {rate} would cause total loss")
            balance *= (1 + rate)
        
        return balance

