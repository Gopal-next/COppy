import click
from project.user import User
from project.transactions import Transaction
from project.reports import Report

class FinanceApp:
    def __init__(self):
        self.current_user = None
        self.setup_database()

    def setup_database(self):
        """Ensure that all necessary tables are created."""
        # print("Creating user table if it doesn't exist...")  
        User.create_user_table()

        Transaction.create_transactions_table()

    def register_user(self, username, password):
        user = User(username, password)
        user.register()

    def login_user(self, username, password):
        user = User(username, password)
        if user.login():
            self.current_user = user
            return True
        return False

    def is_logged_in(self):
        return self.current_user is not None
    
    def add_records(self,user_id,transaction_type,category,amount,date=None): #,description=""
        transaction = Transaction(user_id,transaction_type,category,amount)
        transaction.add_transaction()
    
    def update_records(self,transaction_id,category, amount,date = None):
        Transaction.update_transaction(transaction_id,category, amount,date)

    def delete_records(self,transaction_id):
        Transaction.delete_transaction(transaction_id)


    def all_transaction(self,user_id):
        # all_records = Transaction
        # all_records.view_all_transaction()
        Transaction.view_all_transaction(user_id)


    # Report
    def monthly_review(self,month):
        year = month[:4]  
        report= Report(month=month,year=year)
        report.monthly_report(month)

    def yearly_review(self, year):
        Report.yearly_report(month= None, year = year)

