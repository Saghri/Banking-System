This repository contains a comprehensive banking system designed for a financial institution to manage a wide range of banking operations. The system encompasses functionalities for customer account management, transaction processing, and loan calculations. 

### **Key Features:**

1. **Customer Account Management**:
   - **Account Creation**: Functions to create and manage customer accounts.
   - **Account Details**: Retrieve and update account details such as balance and account status.

2. **Transaction Processing**:
   - **Deposit and Withdrawal**: Functions to handle deposits and withdrawals with validations.
   - **Transaction History**: Maintain and retrieve a history of transactions for each account.

3. **Loan Calculations**:
   - **Interest Rates**: Calculate interest rates on loans based on various parameters.
   - **Loan Repayment**: Functions to compute repayment schedules and total repayment amounts.

### **Implementation Details:**

- **Functions**: Utilizes nested functions to encapsulate and manage variable scope effectively. 
- **Variable Scope**: Careful management of variable scope to ensure data integrity and accurate calculations.
- **Validation**: Includes robust validation mechanisms for transactions and account operations to prevent errors and maintain consistency.

### **Folder Structure:**

- **`src/`**: Contains the main source code files.
  - **`account_management.py`**: Functions related to account creation and management.
  - **`transaction_processing.py`**: Functions for handling transactions and maintaining transaction history.
  - **`loan_calculations.py`**: Functions for calculating loan interest and repayment schedules.
  
- **`tests/`**: Contains unit tests to validate the functionality of the system.
  - **`test_account_management.py`**: Tests for account management functionalities.
  - **`test_transaction_processing.py`**: Tests for transaction processing functionalities.
  - **`test_loan_calculations.py`**: Tests for loan calculation functionalities.

- **`README.md`**: Overview of the project, setup instructions, and usage guidelines.
- **`requirements.txt`**: List of dependencies required to run the project.

### **Usage:**

To get started with the banking system, clone the repository and follow the instructions in the `README.md` file for setup and configuration. The system is designed to be modular and scalable, allowing easy integration of additional features and functionalities as needed.
