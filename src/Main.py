#Auhtor: Jahmari Harrison
#Date: 2-12-2025
#ID: 2304204
#Description: Client menu to navigate the different finacial functions.
#Atrributions: AI was used to provide a more effiecient menu client. reducing lines and increasing 
#               efficiency.

from MaxWithdrawal import MaxWithdrawal
from FixedInvestor import FixedInvestor
from VariableInvestor import VariableInvestor
from RetirementSimulator import RetirementSimulator

def get_input(prompt, type_func=float, min_val=None, max_val=None):
    """Get validated input of specified type."""
    while True:
        try:
            value = type_func(input(prompt))
            
            if min_val is not None and value < min_val:
                print(f"Must be ≥ {min_val}")
                continue
            if max_val is not None and value > max_val:
                
                print(f"Must be ≤ {max_val}")
                continue
                
            return value
        except ValueError:
            print("Invalid input. Try again.")

def run_max_withdrawal():
    print("\n=== Maximum Withdrawal Calculator ===")
    
    balance = get_input("Retirement balance: $", min_val=0.01)
    rate = get_input("Annual return rate (e.g., 0.05): ", min_val=-0.99)
    years = get_input("Years in retirement: ", int, min_val=1)
    
    try:
        calc = MaxWithdrawal(years, balance, rate, 0.01)
        withdrawal = calc.maximum_withdrawal()
        
        print(f"\nResults:")
        print(f"Annual withdrawal: ${withdrawal:,.2f}")
        print(f"Monthly: ${withdrawal/12:,.2f}")
        print(f"Total withdrawn: ${withdrawal * years:,.2f}")
    except Exception as e:
        print(f"Error: {e}")

def run_fixed_investor():
    print("\n=== Fixed Investment Calculator ===")
    
    principal = get_input("Initial investment: $", min_val=0.01)
    years = get_input("Years to invest: ", int, min_val=1)
    rate = get_input("Annual rate (%): ") / 100
    
    try:
        balance = FixedInvestor.fixed_investor(principal, years, rate)
        print(f"\nResults:")
        print(f"Final balance: ${balance:,.2f}")
        print(f"Total gain: ${balance - principal:,.2f}")
    except Exception as e:
        print(f"Error: {e}")

def run_variable_investor():
    print("\n=== Variable Investment ===")
    
    principal = get_input("Initial: $", min_val=0.01)
    years = get_input("Years: ", int, min_val=1)
    
    # Collect rates efficiently
    rates = [get_input(f"Yr{i+1}%: ") / 100 for i in range(years)]
    
    try:
        balance = VariableInvestor.calculate(principal, rates)
        print(f"\nFinal: ${balance:,.2f}")
        print(f"Gain: ${balance - principal:,.2f}")
        
        if years > 1:
            print(f"\nYearly:")
            current = principal
            for i, r in enumerate(rates, 1):
                current *= (1 + r)
                print(f"  {i}: ${current:,.2f} ({r*100:+.1f}%)")
                
    except Exception as e:
        print(f"Error: {e}")

def run_retirement_simulator():
    print("\n=== Retirement Simulator ===")
    
    balance = get_input("Retirement balance: $", min_val=0.01)
    expense = get_input("Annual withdrawal: $", min_val=0.01)
    rate = get_input("Growth rate (%): ") / 100
    
    try:
        sim = RetirementSimulator(balance, expense, rate)
        years = sim.simulate()
        
        print(f"\nResults:")
        print(f"Funds last: {years} years")
        print(f"Withdrawal rate: {(expense/balance)*100:.1f}%")
    except Exception as e:
        print(f"Error: {e}")

def main():
    while True:
        print("\n" + "="*40)
        print("RETIREMENT CALCULATOR")
        print("="*40)
        print("1. Safe Withdrawal Amount")
        print("2. Fixed Investment Growth")
        print("3. Variable Investment Growth")
        print("4. Retirement Fund Duration")
        print("5. Exit")
        print("-"*40)
        
        choice = input("Choose (1-5): ").strip()
        
        match choice:
            case "1":
                run_max_withdrawal()
            case "2":
                run_fixed_investor()
            case "3":
                run_variable_investor()
            case "4":
                run_retirement_simulator()
            case "5":
                print("\nGoodbye!")
                break
            case _:
                print("Invalid choice. Please enter a number between 1-5.")
        
        if choice != "5":
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()