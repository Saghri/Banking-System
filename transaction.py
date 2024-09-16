# transaction.py
class TransactionManager:
    def __init__(self, customer_manager):
        self.customer_manager = customer_manager

    def deposit(self, account_number, amount):
        customer = self.customer_manager.get_customer(account_number)
        if customer is None:
            raise ValueError("Customer does not exist!")
        customer['balance'] += amount
        self.customer_manager.save_customers()

    def withdraw(self, account_number, amount):
        customer = self.customer_manager.get_customer(account_number)
        if customer is None:
            raise ValueError("Customer does not exist!")
        if customer['balance'] < amount:
            raise ValueError("Insufficient funds!")
        customer['balance'] -= amount
        self.customer_manager.save_customers()

    def get_balance(self, account_number):
        customer = self.customer_manager.get_customer(account_number)
        if customer is None:
            raise ValueError("Customer does not exist!")
        return customer['balance']
