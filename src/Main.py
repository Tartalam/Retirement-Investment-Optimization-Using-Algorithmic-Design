from MaxWithdrawal import MaxWithdrawal

def main():
    print("=== Maximum Withdrawal Calculator ===")
    print("Calculate how much you can withdraw annually from your retirement savings\n")
    
    try:
        # Get user input
        balance = float(input("Enter your retirement balance: $"))
        rate = float(input("Enter annual investment return rate (e.g., 0.05 for 5%): "))
        years = int(input("Enter number of years in retirement: "))
        
        # Create calculator and calculate
        calculator = MaxWithdrawal(num_years=years ,balance=balance, rate=rate, tolerance=0.01)
        max_withdrawal = calculator.maximum_withdrawal()
        
        # Display results
        print("\n" + "="*50)
        print("RESULTS:")
        print("="*50)
        print(f"Initial Balance: ${calculator.get_balance:,.2f}")
        print(f"Annual Return Rate: {calculator.get_rate*100:.1f}%")
        print(f"Retirement Period: {calculator.get_num_years} years")
        print(f"Maximum Safe Annual Withdrawal: ${max_withdrawal:,.2f}")
        print(f"Monthly Withdrawal: ${max_withdrawal/12:,.2f}")
        
        # Additional info
        total_withdrawn = max_withdrawal * calculator.get_num_years
        print(f"Total Withdrawn over {calculator.get_num_years} years: ${total_withdrawn:,.2f}")
        
    except ValueError:
        print("Error: Please enter valid numbers!")
    except ZeroDivisionError:
        print("Error: Number of years cannot be zero!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()