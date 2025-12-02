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

