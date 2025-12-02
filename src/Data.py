class Data: 
    def __init__(self):
        self.principal = 0.0
        self.balance = 0.0
        self.years = 0
        self.rate = 0.0

    # Principal Getter and Setter 
    @property
    def principal(self):
        return self.principal

    @principal.setter
    def principal(self, value):
        self.principal = float(value)

    # Balance Getter and Setter 
    @property
    def balance(self):
        return self.balance

    @balance.setter
    def balance(self, value):
        self.balance = float(value)

    # Years Getter and Setter    
    @property
    def years(self):
        return self.years

    @years.setter
    def years(self, value):
        self.years = int(value)
    
    # Rate Getter and Setter 
    @property
    def rate(self):
        return self.rate

    @rate.setter
    def rate(self, value):
        self.rate = float(value)

# Ensure a single shared instance for all the files in the codebase 
data = Data()