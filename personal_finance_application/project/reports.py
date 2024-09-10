import sqlite3

class Report:
    def __init__(self,month, year):
        self.month = month
        self.year = year

    def monthly_report(self,month):
        conn = sqlite3.connect('finance.db')
        cursor = conn.cursor()
        cursor.execute('''
                        SELECT category , SUM(amount) FROM transactions WHERE strftime('%Y-%m', date) = ?
                      GROUP BY category''', (month,))
        report = cursor.fetchall()
        conn.close()
        Total_monthly_income = sum(amount for category, amount in report if category == 'income')
        Total_monthly_expense = sum(amount for category, amount in report if category == 'expense')
        savings = Total_monthly_income - Total_monthly_expense
        print(f"Total Income: {Total_monthly_income}")
        print(f"Total Expense: {Total_monthly_expense}")
        print(f"Savings: {savings}")

    def yearly_report(year):
        conn = sqlite3.connect('finance.db')
        cursor = conn.cursor()
        cursor.execute('''
                        SELECT category , SUM(amount) FROM transactions WHERE strftime('%Y', date) = ?
                      GROUP BY category''', (year,))
        report = cursor.fetchall()
        conn.close()
        Total_yearly_income = sum(amount for category, amount in report if category == 'income')
        Total_yearly_expense = sum(amount for category, amount in report if category == 'expense')
        savings = Total_yearly_income - Total_yearly_expense
        print(f"Total Income: {Total_yearly_income}")
        print(f"Total Expense: {Total_yearly_expense}")
        print(f"Savings: {savings}")

