from project.user import User
from project.transactions import Transaction
from project.reports import Report
from project.budget import Budget
import sqlite3
import datetime as datetime
from project.data_persistence import DatabaseManager

class FinanceApp:
    def __init__(self):
        self.current_user = None
        self.setup_database()

    def setup_database(self):
        """Ensure that all necessary tables are created."""
        # print("Creating user table if it doesn't exist...")  
        User.create_user_table()
        Transaction.create_transactions_table()
        Budget.create_budget()

    def register_user(self, username, password):
        user = User(username, password)
        user.register()

    # def login_user(self, username, password):
    #     user = User(username, password)
    #     if user.login():
    #         self.current_user = user
    #         return True
    #     return False
    def login_user(self, username, password):
        user = User.login(username)  # Get the user data from the database
        if user and user['password'] == password:
            return user['id']  # Return the user ID if login is successful
        else:
            raise ValueError("Invalid username or password")


    def is_logged_in(self):
        return self.current_user is not None
    
    def fetch_category(self, user_id ,type):
        Transaction.fetch_by_category(user_id,type)

    
    # def add_records(self,user_id,type,category,amount,date=None): #,description=""
    #     if amount is None or amount <= 0:
    #         raise ValueError("Amount must be a positive number.")
    #     print(f"Received amount: {amount}") 
    #     transaction = Transaction(user_id,type,category,amount,date)
    #     transaction.add_transaction()
    
    def add_records(self, user_id, type, category, amount, date=None):  # ,description=""
        if amount is None or amount <= 0:
            raise ValueError("Amount must be a positive number.")
        
        print(f"Received amount: {amount}")
        
        # Add the transaction first
        transaction = Transaction(user_id, type, category, amount, date)
        transaction.add_transaction()

        # After adding the transaction, check if the user exceeded their budget
        if type == 'expense':  # Only check budget for expenses
            conn = sqlite3.connect('finance.db')
            cursor = conn.cursor()

            # Fetch the monthly budget for the given category and month
            current_month = datetime.now().strftime('%Y-%m')  # Get current month
            cursor.execute('''
                SELECT monthly_budget 
                FROM budget 
                WHERE user_id = ? AND category = ? AND month = ?''', 
                (user_id, category, current_month))
            
            budget = cursor.fetchone()
            
            if budget:
                monthly_budget = budget[0]
                # Fetch the total expenses for the month and category
                cursor.execute('''
                    SELECT SUM(amount) 
                    FROM transactions 
                    WHERE user_id = ? AND category = ? AND transaction_type = 'expense' AND substr(date, 1, 7) = ?''', 
                    (user_id, category, current_month))
                
                total_expense = cursor.fetchone()[0]

                # Compare total expense with budget
                if total_expense > monthly_budget:
                    print(f"Warning: You have exceeded your budget limit for {category} this month!")
                    print(f"Total Expense: {total_expense}, Budget Limit: {monthly_budget}")
                    # Optionally, prompt the user to update or delete the transaction
                    user_input = input("Do you want to update or delete this transaction? (update/delete/none): ").lower()
                    if user_input == "update":
                        self.update_records(user_id, category, amount)  # Add your update function here
                    elif user_input == "delete":
                        self.delete_records(user_id)  # Add your delete function here

        conn.close()

    def update_records(self,transaction_id,category, amount,date = None):
        Transaction.update_transaction(transaction_id,category, amount,date)

    def delete_records(self,transaction_id):
        Transaction.delete_transaction(transaction_id)


    def all_transaction(self,user_id):
        # all_records = Transaction
        # all_records.view_all_transaction()
        Transaction.view_all_transaction(user_id)

    def see_all_budegt(self,user_id):
        # all_records = Transaction
        # all_records.view_all_transaction()
        Budget.view_budget(user_id)

    # Report
    def monthly_review(self,user_id,month):
        year = month[:4]  
        report= Report(user_id,month=month,year=year)
        report.monthly_report(month)

    def yearly_review(self,user_id, year):
        report = Report(user_id,year=year)
        report.yearly_report(year)

    # budget
    def budget_set(self,user_id, month, category, monthly_budget):
        set = Budget(user_id, month, category, monthly_budget)
        set.set_budget()
        

    def budget_check(self,user_id , category, month):
        check = Budget(user_id, category, month)
        check.check_budget(user_id, category, month)

    def get_notify():
        notify = Budget()
        notify.notify_users()
