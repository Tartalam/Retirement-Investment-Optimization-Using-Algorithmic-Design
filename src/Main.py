from MaxWithdrawal import MaxWithdrawal
from FixedInvestor import FixedInvestor
from VariableInvestor import variableInvestor

def run_max_withdrawal():
    print("\n=== Maximum Withdrawal Calculator ===")

    balance = float(input("Enter your retirement balance: $"))
    rate = float(input("Enter annual investment return rate (e.g., 0.05): "))
    years = int(input("Enter number of years in retirement: "))

    calculator = MaxWithdrawal(balance=balance, rate=rate, num_years=years, tolerance=0.01)
    max_withdrawal = calculator.maximum_withdrawal()

    print("\n=== RESULTS ===")
    print(f"Initial Balance: ${calculator.get_balance():,.2f}")
    print(f"Annual Return Rate: {calculator.get_rate()*100:.1f}%")
    print(f"Retirement Period: {calculator.get_num_years()} years")
    print(f"Maximum Safe Annual Withdrawal: ${max_withdrawal:,.2f}")
    print(f"Monthly Withdrawal: ${max_withdrawal/12:,.2f}")

    total_withdrawn = max_withdrawal * calculator.get_num_years()
    print(f"Total Withdrawn: ${total_withdrawn:,.2f}")


def run_fixed_investor():
    print("\n=== Fixed Investor Function ===")

    principal = float(input("Enter your initial investment amount: $"))
    years = int(input("Enter the number of years until retirement: "))
    rate = float(input("Enter the interest rate (percent): "))

    balance = FixedInvestor.fixed_investor(principal, rate / 100, years)
    amount_gained = balance - principal

    print("\n=== RESULTS ===")
    print(f"Initial investment: ${principal:,.2f}")
    print(f"Years until retirement: {years}")
    print(f"Fixed interest rate: {rate}%")
    print(f"Final Balance: ${balance:,.2f}")
    print(f"You gained: ${amount_gained:,.2f}")


def run_variable_investor():
    print("\n=== Variable Investor Function ===")

    principal = float(input("Enter your initial investment amount: $"))
    n = int(input("Enter the number of years: "))

    rateList = []
    print("\nEnter each year's rate (e.g., 0.05 for 5%):")
    for i in range(n):
        rate = float(input(f"Year {i+1} rate: "))
        rateList.append(rate)

    balance = variableInvestor(principal, rateList)
    gain = balance - principal

    print("\n=== RESULTS ===")
    print(f"Initial investment: ${principal:,.2f}")
    print(f"Final balance: ${balance:,.2f}")
    print(f"Total gain: ${gain:,.2f}")


def main():
    print("=== Retirement Calculator ===")
    print("1. Maximum Withdrawal Calculator")
    print("2. Fixed Investment Calculator")
    print("3. Variable Investment Calculator")

    choice = input("Choose an option (1, 2 or 3): ")

    try:
        if choice == "1":
            run_max_withdrawal()
        elif choice == "2":
            run_fixed_investor()
        elif choice == "3":
            run_variable_investor()
        else:
            print("Invalid option selected.")

    except ValueError:
        print("Error: Invalid numeric input.")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()