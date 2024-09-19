import sqlite3
from datetime import datetime
class Transaction:
    def __init__(self,user_id,type,transaction_type,category,amount,date=None): #,description=""
        self.user_id =  user_id
        self.type = type
        self.transaction_type = transaction_type
        self.category = category
        self.amount = amount
        self.date =datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # self.description = description


    @staticmethod
    def create_transactions_table(): #description TEXT,
        conn = sqlite3.connect('finance.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                type TEXT NOT NULL,
                category TEXT NOT NULL,
                amount REAL NOT NULL,
                date TIMESTAMP,

                FOREIGN KEY (user_id) REFERENCES users(id)
            );
        ''')
        conn.commit()
        conn.close()

    def add_transaction(self):
        conn = sqlite3.connect('finance.db') #,description
        cursor = conn.cursor()
        cursor.execute('''
                       INSERT INTO transactions (user_id,type,category,amount,date) 
                       VALUES (?,?,?,?,?)''',
                       (self.user_id, self.transaction_type,self.category,self.amount,self.date)) #,self.description
        conn.commit()
        conn.close()

    def update_transaction(id,category, amount,date= None):
        conn = sqlite3.connect('finance.db')
        cursor = conn.cursor()
        cursor.execute('''
                        UPDATE transactions 
                       SET category = ?, amount = ?, date = ?
                       WHERE id = ?''', (category, amount,id,date))
        conn.commit()
        conn.close() #, description = ?  ,description
        
    @staticmethod
    def delete_transaction(transaction_id):
        conn = sqlite3.connect('finance.db')
        cursor = conn.cursor()
        cursor.execute('''
                        DELETE FROM transactions where id = ?''',(transaction_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def view_all_transaction(user_id):
        conn = sqlite3.connect('finance.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM users WHERE id = ?', (user_id,))
        user_exists = cursor.fetchone()[0]

        if user_exists == 0:
            raise ValueError("User ID does not exist.")
        
        cursor.execute('''
                        SELECT * from transactions where user_id = ?''',(user_id,))
        transactions = cursor.fetchall()
        # print(transactions)
        conn.close()
        for transaction in transactions:
            print(f"ID : {transaction[0]}, User ID : {transaction[1]} Type : {transaction[2]}, Category : {transaction[3]}, Amount : {transaction[4]}, Date : {transaction[5]} ")
    

    def fetch_by_category(user_id,type):
        conn = sqlite3.connect('finance.db')
        cursor = conn.cursor()

        cursor.execute(''' SELECT category , SUM(amount) FROM transactions where user_id = ? and type = ? GROUP by category 
                    ''', (user_id,type,))
        
        fetch = cursor.fetchall()
        conn.close()
        Total = 0
        for category , total_amount in fetch:
            print(f"Category : {category}, Total Amount : {total_amount}")
            Total += total_amount
        print("Overall amount ", Total)