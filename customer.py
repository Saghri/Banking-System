# customer.py
import json

class Customer:
    def __init__(self, account_number, name, balance, contact_info):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.contact_info = contact_info

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "name": self.name,
            "balance": self.balance,
            "contact_info": self.contact_info
        }

class CustomerManager:
    def __init__(self):
        self.customers = self.load_customers()

    def load_customers(self):
        try:
            with open('customers.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_customers(self):
        with open('customers.json', 'w') as file:
            json.dump(self.customers, file)

    def add_customer(self, account_number, name, balance, contact_info):
        if account_number in self.customers:
            raise ValueError("Account number already exists!")
        self.customers[account_number] = Customer(account_number, name, balance, contact_info).to_dict()
        self.save_customers()

    def delete_customer(self, account_number):
        if account_number not in self.customers:
            raise ValueError("Customer does not exist!")
        del self.customers[account_number]
        self.save_customers()

    def get_customer(self, account_number):
        return self.customers.get(account_number, None)
    
    def get_customer_details(self, account_number):
        customer = self.customers.get(account_number)
        if not customer:
            raise ValueError("Customer does not exist!")
        return (f"Account Number: {customer['account_number']}\n"
                f"Name: {customer['name']}\n"
                f"Balance: {customer['balance']}\n"
                f"Contact Info: {customer['contact_info']}")
