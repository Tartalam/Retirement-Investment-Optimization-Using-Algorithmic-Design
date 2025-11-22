def variable_investor(principal, rateList):

    """
    Simulates growth with variable annual interest rates.
    
    Args:
        principal (float): Starting investment value.
        rateList (list of float): List of annual growth rates (e.g., [0.05, 0.07, -0.02] for 5%, 7%, -2%).
    
    Returns:
        float: Final accumulated balance after applying all rates.
    """
    
    if principal <= 0:
        raise ValueError("Principal must be positive.")
    if not rateList:
        return principal

    balance = principal
    for r in rateList:
        if r <= -1:
            raise ValueError("Interest rate <= -1 causes total loss.")
        balance *= (1 + r)
    return balance


