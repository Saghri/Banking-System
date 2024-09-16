# loan.py
class Loan:
    def __init__(self, loan_type, principal, rate, term):
        self.loan_type = loan_type
        self.principal = principal
        self.rate = rate / 100
        self.term = term

    def calculate_simple_interest(self):
        return self.principal * self.rate * self.term

    def calculate_total_amount(self):
        return self.principal + self.calculate_simple_interest()

class LoanManager:
    def create_loan(self, loan_type, principal, rate, term):
        loan = Loan(loan_type, principal, rate, term)
        return loan.calculate_total_amount()
