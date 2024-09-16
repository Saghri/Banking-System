# gui.py
import tkinter as tk
from tkinter import messagebox
from customer import CustomerManager
from transaction import TransactionManager
from loan import LoanManager

class BankingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Banking System")
        self.customer_manager = CustomerManager()
        self.transaction_manager = TransactionManager(self.customer_manager)
        self.loan_manager = LoanManager()
        self.create_widgets()

    def create_widgets(self):
        # Frame for customer operations
        customer_frame = tk.Frame(self.root)
        customer_frame.pack(pady=10)

        # Account Number
        tk.Label(customer_frame, text="Account Number:").grid(row=0, column=0)
        self.acc_number = tk.Entry(customer_frame)
        self.acc_number.grid(row=0, column=1)

        # Name
        tk.Label(customer_frame, text="Name:").grid(row=1, column=0)
        self.name = tk.Entry(customer_frame)
        self.name.grid(row=1, column=1)

        # Balance
        tk.Label(customer_frame, text="Balance:").grid(row=2, column=0)
        self.balance = tk.Entry(customer_frame)
        self.balance.grid(row=2, column=1)

        # Contact Info
        tk.Label(customer_frame, text="Contact Info:").grid(row=3, column=0)
        self.contact_info = tk.Entry(customer_frame)
        self.contact_info.grid(row=3, column=1)

        # Buttons for customer operations
        tk.Button(customer_frame, text="Add Customer", command=self.add_customer).grid(row=4, column=0, columnspan=2, pady=5)
        tk.Button(customer_frame, text="Delete Customer", command=self.delete_customer).grid(row=5, column=0, columnspan=2)

        # Frame for transactions
        transaction_frame = tk.Frame(self.root)
        transaction_frame.pack(pady=10)

        # Deposit
        tk.Label(transaction_frame, text="Amount to Deposit:").grid(row=0, column=0)
        self.deposit_amount = tk.Entry(transaction_frame)
        self.deposit_amount.grid(row=0, column=1)
        tk.Button(transaction_frame, text="Deposit", command=self.deposit).grid(row=1, column=0, columnspan=2)

        # Withdraw
        tk.Label(transaction_frame, text="Amount to Withdraw:").grid(row=2, column=0)
        self.withdraw_amount = tk.Entry(transaction_frame)
        self.withdraw_amount.grid(row=2, column=1)
        tk.Button(transaction_frame, text="Withdraw", command=self.withdraw).grid(row=3, column=0, columnspan=2)

        # Frame for loan
        loan_frame = tk.Frame(self.root)
        loan_frame.pack(pady=10)

        # Loan Amount
        tk.Label(loan_frame, text="Loan Amount:").grid(row=0, column=0)
        self.loan_amount = tk.Entry(loan_frame)
        self.loan_amount.grid(row=0, column=1)

        # Interest Rate
        tk.Label(loan_frame, text="Interest Rate (%):").grid(row=1, column=0)
        self.loan_rate = tk.Entry(loan_frame)
        self.loan_rate.grid(row=1, column=1)

        # Term
        tk.Label(loan_frame, text="Term (years):").grid(row=2, column=0)
        self.loan_term = tk.Entry(loan_frame)
        self.loan_term.grid(row=2, column=1)

        # Calculate Loan
        tk.Button(loan_frame, text="Calculate Loan", command=self.calculate_loan).grid(row=3, column=0, columnspan=2)

    def add_customer(self):
        try:
            account_number = self.acc_number.get()
            name = self.name.get()
            balance = float(self.balance.get())
            contact_info = self.contact_info.get()
            self.customer_manager.add_customer(account_number, name, balance, contact_info)
            messagebox.showinfo("Success", "Customer added successfully!")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def delete_customer(self):
        try:
            account_number = self.acc_number.get()
            self.customer_manager.delete_customer(account_number)
            messagebox.showinfo("Success", "Customer deleted successfully!")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def deposit(self):
        try:
            account_number = self.acc_number.get()
            amount = float(self.deposit_amount.get())
            self.transaction_manager.deposit(account_number, amount)
            messagebox.showinfo("Success", "Deposit successful!")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def withdraw(self):
        try:
            account_number = self.acc_number.get()
            amount = float(self.withdraw_amount.get())
            self.transaction_manager.withdraw(account_number, amount)
            messagebox.showinfo("Success", "Withdrawal successful!")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def calculate_loan(self):
        try:
            loan_amount = float(self.loan_amount.get())
            rate = float(self.loan_rate.get())
            term = int(self.loan_term.get())
            total = self.loan_manager.create_loan("personal", loan_amount, rate, term)
            messagebox.showinfo("Loan Calculation", f"Total loan amount with interest: {total}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = BankingApp(root)
    root.mainloop()
