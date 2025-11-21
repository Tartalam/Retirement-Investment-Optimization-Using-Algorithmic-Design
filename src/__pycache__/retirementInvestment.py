def finallyRetired(balance, expense, rate):
    """
    Simulate how long retirement funds last given
    fixed annual withdrawals and an annual growth rate.
    
    Parameters:
        balance (float): initial retirement savings
        expense (float): fixed annual withdrawal amount
        rate (float): annual interest rate (e.g., 0.05 for 5%)
    
    Returns:
        int: number of years until balance is depleted (<= 0)
    """
    years = 0
    while balance > 0:
        balance = balance * (1 + rate) - expense
        years += 1
        
      
        if years > 200:  
            return float('inf')  
    
    return years
