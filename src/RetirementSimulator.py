class RetirementSimulator:
    def __init__(self, balance, expense, rate):
        try:
            # Validate types
            if not isinstance(balance, (int, float)):
                raise TypeError("Balance must be a number.")
            if not isinstance(expense, (int, float)):
                raise TypeError("Expense must be a number.")
            if not isinstance(rate, (int, float)):
                raise TypeError("Rate must be a number.")

            # Validate values
            if balance < 0:
                raise ValueError("Balance cannot be negative.")
            if expense < 0:
                raise ValueError("Expense cannot be negative.")
            if rate < 0:
                raise ValueError("Rate cannot be negative.")

            self.initial_balance = balance
            self.balance = balance
            self.expense = expense
            self.rate = rate
            self.years = 0

        except Exception as e:
            print(f"Error during initialization: {e}")
            raise


    def simulate(self):
        try:
            if self.expense == 0 and self.rate >= 0:
                return float('Money last forever')  # Money lasts forever
            
            while self.balance > 0:
                self.balance = self.balance * (1 + self.rate) - self.expense
                self.years += 1

                if self.years > 200:
                    raise RuntimeError("Simulation exceeded 200 years—possible infinite loop.")
            
            return self.years

        except Exception as e:
            print(f"Simulation error: {e}")
            return None


    def summary(self):
        try:
            print(f"Initial Balance: ${self.initial_balance:,.2f}")
            print(f"Annual Withdrawal: ${self.expense:,.2f}")
            print(f"Growth Rate: {self.rate * 100:.2f}%")

            if self.years == float('inf'):
                print("Funds last indefinitely.")
            else:
                print(f"Funds last for approximately {self.years} years.")

        except Exception as e:
            print(f"Error printing summary: {e}")


