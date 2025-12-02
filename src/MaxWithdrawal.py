# Author: Jahmari Harrison
# Date: 28-11-2025
# Description: Generate max withdrawal amount last last over a fixed retirement period.
#Attribution: the Documentation and exeption handling was done with the help of AI.
from Data import data
class MaxWithdrawal:

    
    def __init__(self, num_years, balance, rate, tolerance=0.1):
       
        if not isinstance(num_years, int):
            raise TypeError("num_years must be an integer")
        if num_years <= 0:
            raise ValueError("num_years must be positive")
        if not isinstance(tolerance, (int, float)):
            raise TypeError("tolerance must be a number")
        if tolerance <= 0:
            raise ValueError("tolerance must be positive")
        # Input validation
        if not isinstance(balance, (int, float)):
            raise TypeError("balance must be a number")
        if balance <= 0:
            raise ValueError("balance must be positive")
        if not isinstance(rate, (int, float)):
            raise TypeError("rate must be a number")
        if rate <= -1:
            raise ValueError("rate must be greater than -1 (100% loss)")
        
            
        self.__num_years = data.years 
        self.__tolerance = tolerance
        self.__balance = data.balance
        self.__rate = data.rate
        
    
    def maximum_withdrawal(self):
        

        try:
            # Calculate initial high bound using annuity formula
            # This provides an upper bound for the binary search
            denominator = 1 - (1 + self.__rate) ** (-self.__num_years)
            
            # Check for division by zero or invalid denominator
            if abs(denominator) < 1e-10:  # Very small denominator
                if self.__rate == 0:
                    # Special case: zero interest rate
                    high = self.__balance / self.__num_years
                else:
                    raise ValueError("Invalid parameters for annuity calculation")
            else:
                high = (self.__balance * self.__rate) / denominator
            
            # Validate the calculated high bound
            if high <= 0 or not isinstance(high, (int, float)):
                raise ValueError("Failed to calculate valid initial withdrawal estimate")
                
            low = 0
            
            return self.__binary_search_withdrawal(self.__balance, self.__rate, low, high, self.__tolerance, self.__num_years)
            
        except (OverflowError, ValueError) as e:
            raise ValueError(f"Withdrawal calculation failed: {str(e)}") from e
    
    def __binary_search_withdrawal(self, balance, rate, low, high, tolerance, years):
        
        # Base case: search range is within tolerance
        if (high - low) <= tolerance:
            return (low + high) / 2
        
        # Safety check for infinite recursion
        if high <= low:
            raise ValueError("Binary search failed: high bound <= low bound")
        
        mid = (low + high) / 2
        
        try:
            final_balance = self.__simulate_retirement(balance, rate, mid, years)
        except Exception as e:
            raise ValueError(f"Retirement simulation failed: {str(e)}") from e
        
        # Recursive cases
        if final_balance >= 0:
            # Withdrawal is sustainable, try higher amount
            return self.__binary_search_withdrawal(balance, rate, mid, high, tolerance, years)
        else:
            # Withdrawal is too high, try lower amount
            return self.__binary_search_withdrawal(balance, rate, low, mid, tolerance, years)
    
    def __simulate_retirement(self, initial_balance, rate, withdrawal, years):
       
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("initial_balance must be a non-negative number")
        if not isinstance(withdrawal, (int, float)) or withdrawal < 0:
            raise ValueError("withdrawal must be a non-negative number")
        if not isinstance(years, int) or years <= 0:
            raise ValueError("years must be a positive integer")
        
        current_balance = initial_balance
        
        try:
            for year in range(years):
                # Withdraw annual amount
                current_balance -= withdrawal
                
                # Check if portfolio is depleted
                if current_balance < 0:
                    # Portfolio ran out of money - return negative balance
                    return current_balance
                
                # Apply investment returns
                current_balance *= (1 + rate)
                
                # Safety check for numerical instability
                if not isinstance(current_balance, (int, float)):
                    raise ValueError("Simulation produced invalid balance value")
                    
            return current_balance
            
        except (OverflowError, ValueError) as e:
            raise ValueError(f"Retirement simulation error: {str(e)}") from e
    
    @property
    def get_num_years(self):
        """Get the number of retirement years."""
        return self.__num_years
    
    @property
    def get_tolerance(self):
        """Get the binary search tolerance."""
        return self.__tolerance
    
    @property
    def get_balance(self):
        """Get the balance for the user account"""
        return self.__balance
    
    @property
    def get_rate(self):
        """Get the Interest rate"""
        return self.__rate
    
    
