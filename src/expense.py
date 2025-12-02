class RetirementSimulator:
    def __init__(self, balance, expense, rate):
        self.initial_balance = balance
        self.balance = balance
        self.expense = expense
        self.rate = rate
        self.years = 0

    def simulate(self):
        while self.balance > 0:
            self.balance = self.balance * (1 + self.rate) - self.expense
            self.years += 1
            if self.years > 200:
                return float('inf')
        return self.years

    def summary(self):
        print(f"Initial Balance: ${self.initial_balance:,.2f}")
        print(f"Annual Withdrawal: ${self.expense:,.2f}")
        print(f"Growth Rate: {self.rate * 100:.2f}%")
        print(f"Funds last for approximately {self.years} years.")


# --- RUN THE SIMULATION ---
simulator = RetirementSimulator(1_000_000, 80_000, 0.05)
years = simulator.simulate()
print(f"The retirement fund lasts for {years} years.")
simulator.summary()
