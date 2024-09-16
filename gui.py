import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from customer import CustomerManager
from transaction import TransactionManager
from loan import LoanManager

class BankingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Banking System")
        self.root.geometry("700x600")  # Set initial window size
        self.customer_manager = CustomerManager()
        self.transaction_manager = TransactionManager(self.customer_manager)
        self.loan_manager = LoanManager()

        # Create a canvas and a scrollbar
        self.canvas = tk.Canvas(root)
        self.scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.config(yscrollcommand=self.scrollbar.set)

        self.create_widgets()

    def create_widgets(self):
        # Styling for ttk widgets
        style = ttk.Style()
        style.configure('TLabel', padding=5)
        style.configure('TButton', padding=5)
        style.configure('TEntry', padding=5)
        style.configure('TText', padding=5)

        # Frame for Customer Operations
        customer_frame = ttk.Frame(self.scrollable_frame, padding="15")
        customer_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ttk.Label(customer_frame, text="Account Number:").grid(row=0, column=0, sticky="w")
        self.acc_number = ttk.Entry(customer_frame, width=30)
        self.acc_number.grid(row=0, column=1, sticky="ew")

        ttk.Label(customer_frame, text="Name:").grid(row=1, column=0, sticky="w")
        self.name = ttk.Entry(customer_frame, width=30)
        self.name.grid(row=1, column=1, sticky="ew")

        ttk.Label(customer_frame, text="Balance:").grid(row=2, column=0, sticky="w")
        self.balance = ttk.Entry(customer_frame, width=30)
        self.balance.grid(row=2, column=1, sticky="ew")

        ttk.Label(customer_frame, text="Contact Info:").grid(row=3, column=0, sticky="w")
        self.contact_info = ttk.Entry(customer_frame, width=30)
        self.contact_info.grid(row=3, column=1, sticky="ew")

        ttk.Button(customer_frame, text="Add Customer", command=self.add_customer).grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")
        ttk.Button(customer_frame, text="Delete Customer", command=self.delete_customer).grid(row=5, column=0, columnspan=2, pady=10, sticky="ew")
        ttk.Button(customer_frame, text="View Customer Details", command=self.view_customer_details).grid(row=6, column=0, columnspan=2, pady=10, sticky="ew")

        # Frame for Transaction Operations
        transaction_frame = ttk.Frame(self.scrollable_frame, padding="15")
        transaction_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        ttk.Label(transaction_frame, text="Amount to Deposit:").grid(row=0, column=0, sticky="w")
        self.deposit_amount = ttk.Entry(transaction_frame, width=30)
        self.deposit_amount.grid(row=0, column=1, sticky="ew")

        ttk.Button(transaction_frame, text="Deposit", command=self.deposit).grid(row=1, column=0, columnspan=2, pady=10, sticky="ew")

        ttk.Label(transaction_frame, text="Amount to Withdraw:").grid(row=2, column=0, sticky="w")
        self.withdraw_amount = ttk.Entry(transaction_frame, width=30)
        self.withdraw_amount.grid(row=2, column=1, sticky="ew")

        ttk.Button(transaction_frame, text="Withdraw", command=self.withdraw).grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")

        # Frame for Loan Calculations
        loan_frame = ttk.Frame(self.scrollable_frame, padding="15")
        loan_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        ttk.Label(loan_frame, text="Loan Amount:").grid(row=0, column=0, sticky="w")
        self.loan_amount = ttk.Entry(loan_frame, width=30)
        self.loan_amount.grid(row=0, column=1, sticky="ew")

        ttk.Label(loan_frame, text="Interest Rate (%):").grid(row=1, column=0, sticky="w")
        self.loan_rate = ttk.Entry(loan_frame, width=30)
        self.loan_rate.grid(row=1, column=1, sticky="ew")

        ttk.Label(loan_frame, text="Term (years):").grid(row=2, column=0, sticky="w")
        self.loan_term = ttk.Entry(loan_frame, width=30)
        self.loan_term.grid(row=2, column=1, sticky="ew")

        ttk.Button(loan_frame, text="Calculate Loan", command=self.calculate_loan).grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")

        # Frame for Customer Details
        details_frame = ttk.Frame(self.scrollable_frame, padding="15")
        details_frame.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

        ttk.Label(details_frame, text="Customer Details:").grid(row=0, column=0, sticky="w")
        self.customer_details = tk.Text(details_frame, width=80, height=10, wrap=tk.WORD)
        self.customer_details.grid(row=1, column=0, sticky="nsew")
        self.customer_details.config(state=tk.DISABLED)  # Make text area read-only

        # Adjust row/column weights
        self.scrollable_frame.grid_rowconfigure(0, weight=1)
        self.scrollable_frame.grid_rowconfigure(1, weight=1)
        self.scrollable_frame.grid_rowconfigure(2, weight=1)
        self.scrollable_frame.grid_rowconfigure(3, weight=1)
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

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

    def view_customer_details(self):
        try:
            account_number = self.acc_number.get()
            details = self.customer_manager.get_customer_details(account_number)
            self.customer_details.config(state=tk.NORMAL)
            self.customer_details.delete(1.0, tk.END)
            self.customer_details.insert(tk.END, details)
            self.customer_details.config(state=tk.DISABLED)
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
