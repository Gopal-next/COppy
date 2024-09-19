import sqlite3

class Report:
    def __init__(self,month=None, year=None):
        self.month = month
        self.year = year

    def monthly_report(self,month):
        conn = sqlite3.connect('finance.db')
        cursor = conn.cursor()
        print(f"Fetching transactions for month: {month}")
        cursor.execute('''
                        SELECT type , SUM(amount) FROM transactions WHERE strftime('%Y-%m', date) = ?
                        GROUP BY type''', (month,))
        report = cursor.fetchall()
        conn.close()
        print(f"Fetched data: {report}")
        income_categories = ['income', 'salary']
    # Categories considered as expense
        expense_categories = ['expense', 'food', 'drink']
        Total_monthly_income = sum(amount for t, amount in report if t in income_categories)
        Total_monthly_expense = sum(amount for t, amount in report if t in expense_categories)
        savings = Total_monthly_income - Total_monthly_expense
        print(f"Total Income: {Total_monthly_income}")
        print(f"Total Expense: {Total_monthly_expense}")
        print(f"Savings: {savings}")

    def yearly_report(self, year):
        conn = sqlite3.connect('finance.db')
        cursor = conn.cursor()
        cursor.execute('''
                        SELECT type, SUM(amount) FROM transactions WHERE strftime('%Y', date) = ?
                      GROUP BY type''', (year,))
        report = cursor.fetchall()
        conn.close()
        print(f"Fetched data: {report}")
        Total_yearly_income = sum(amount for t, amount in report if t == 'income')
        Total_yearly_expense = sum(amount for t, amount in report if t == 'expense')
        savings = Total_yearly_income - Total_yearly_expense
        print(f"Total Income: {Total_yearly_income}")
        print(f"Total Expense: {Total_yearly_expense}")
        print(f"Savings: {savings}")


