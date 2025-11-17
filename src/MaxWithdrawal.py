class MaxWithdrawal:
    """
    A class to calculate the maximum safe annual withdrawal amount from retirement savings
    using a binary search algorithm to find the optimal withdrawal rate.
    
    The class determines the maximum amount that can be withdrawn annually from a retirement
    portfolio over a fixed period while ensuring the portfolio doesn't run out of money,
    taking into account expected investment returns.
    
    Attributes:
        __num_years (int): Number of years in retirement (must be positive)
        __tolerance (float): Precision tolerance for binary search convergence (default: 0.1)
    """
    
    def __init__(self, num_years, balance, rate, tolerance=0.1):
        """
        Initialize the MaxWithdrawal calculator with retirement parameters.
        
        Args:
            num_years (int): Number of years in retirement (must be positive)
            tolerance (float, optional): Precision tolerance for binary search. Defaults to 0.1.
            
        Raises:
            ValueError: If num_years is not positive or tolerance is not positive
            TypeError: If num_years is not an integer or tolerance is not a number
        """
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
        
            
        self.__num_years = num_years
        self.__tolerance = tolerance
        self.__balance = balance
        self.__rate = rate
        
    
    def maximum_withdrawal(self):
        """
        Calculate the maximum safe annual withdrawal amount.
        
        Uses a binary search algorithm to find the maximum annual withdrawal that
        allows the portfolio to last for the specified number of years.
        
        Args:
            balance (float): Initial retirement portfolio balance (must be positive)
            rate (float): Expected annual investment return rate as a decimal (e.g., 0.05 for 5%)
            
        Returns:
            float: Maximum safe annual withdrawal amount
            
        Raises:
            ValueError: If balance is not positive, rate is not valid, or calculation fails
            TypeError: If balance or rate are not numbers
            ZeroDivisionError: If the annuity formula calculation fails (e.g., rate = -1)
        """

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
        """
        Recursive binary search to find the optimal withdrawal amount.
        
        Args:
            balance (float): Initial portfolio balance
            rate (float): Annual investment return rate
            low (float): Lower bound of search range
            high (float): Upper bound of search range
            tolerance (float): Convergence tolerance
            years (int): Number of years
            
        Returns:
            float: Optimal withdrawal amount within specified tolerance
            
        Raises:
            RecursionError: If binary search fails to converge (excessive recursion)
        """
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
        """
        Simulate retirement withdrawals over the specified period.
        
        Args:
            initial_balance (float): Starting portfolio balance
            rate (float): Annual investment return rate
            withdrawal (float): Annual withdrawal amount
            years (int): Number of years to simulate
            
        Returns:
            float: Final portfolio balance after all years
            
        Raises:
            ValueError: If simulation produces invalid results
        """
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
    
    
    def __str__(self):
        return f"Retirement Calculator: ${self.__balance:,.2f} for {self.__num_years} years at {self.__rate*100}%"
    
    def __repr__(self):
        return f"MaxWithdrawal(num_years={self.__num_years}, balance={self.__balance}, rate={self.__rate}, tolerance={self.__tolerance})"
