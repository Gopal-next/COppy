import sqlite3

class Budget:
    def __init__(self,user_id, month, category, monthly_budget, budget_id=None):
        self.budget_id = budget_id
        self.user_id= user_id
        self.month = month
        self.category = category
        self.monthly_budget= monthly_budget

    @staticmethod
    def create_budget():
        conn = sqlite3.connect('finance.db')
        cursor = conn.cursor()

        cursor.execute(''' CREATE TABLE if not EXISTS budget (
                       budget_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       user_id INTEGER NOT NULL,
                       month TEXT NOT NULL ,
                       category text NOT NULL,
                       monthly_budget REAL NOT NULL,
                       FOREIGN KEY (user_id) REFERENCES users(user_id)
                       );
                        ''')
        
        conn.commit()
        conn.close()

    # @staticmethod
    def set_budget(self):
        conn = sqlite3.connect('finance.db')
        cursor = conn.cursor()

        cursor.execute('''
                        SELECT monthly_budget FROM budget where user_id = ?  and month = ? and category = ? ''', 
                        (self.user_id, self.month, self.category)
                        )
        budget = cursor.fetchone()

        if budget:
            print(f"Budget Already set for {self.category} for {self.month}")
            # print("You want it to update it by value put by you as above, type 'YES' for updation or 'NO'")
            user_input = input("You want it to update it by value put by you as above, type 'YES' for updation or 'NO' \
                         \n Type 'YES/NO' ").lower()
            if user_input == 'yes':
                cursor.execute('''
                               UPDATE budget
                               SET monthly_budget = ? 
                               WHERE user_id = ? and category = ? and month = ?''', 
                               (self.monthly_budget,self.user_id, self.category, self.month))
            else:
                print("NO change for budget")
        
        else:
            print(f"Budget setting for {self.category} for {self.month}")
            cursor.execute('''
                        INSERT INTO budget (user_id,  month, category , monthly_budget) VALUES (?, ?, ?, ?)''', 
                        (self.user_id, self.month, self.category, self.monthly_budget))
        conn.commit()
        conn.close()

    # def set_budget(self):
    #     conn = sqlite3.connect('finance.db') #,description
    #     cursor = conn.cursor()
    #     cursor.execute('''
    #                 SELECT COUNT(*) FROM budget WHERE user_id = ? AND month = ? AND category = ?''', 
    #                 (self.user_id, self.month, self.category))
    #     user_exists = cursor.fetchone()[0]
    #     # user = cursor.fetchall()
        

    #     if user_exists == 0:
    #         cursor.execute('''
    #                     INSERT INTO budget (user_id,  month, category , monthly_budget) VALUES (?, ?, ?, ?)''',
    #                     (self.user_id, self.month, self.category, self.monthly_budget)) #,self.description
    #         conn.commit()
    #     else:
    #         raise ValueError("User id alreday exist")
    #     conn.close()
        # print('user :', user)
    
    
    @staticmethod
    def view_budget(user_id):
        conn = sqlite3.connect('finance.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM budget WHERE user_id = ?', (user_id,))
        user_exists = cursor.fetchone()[0]

        if user_exists == 0:
            raise ValueError("User ID does not exist.")
        
        cursor.execute('''
                        SELECT * from budget where user_id = ?''',(user_id,)
                        )
        budgets  = cursor.fetchall()
        conn.close()
        for budget in budgets :
            print(f"ID : {budget[0]}, User ID : {budget[1]} Type : {budget[2]}, Category : {budget[3]} , set_amount : {budget[4]}")


    @staticmethod
    def check_budget(self):
        conn = sqlite3.connect('finance.db')
        cursor = conn.cursor()

        cursor.execute('''
                        SELECT monthly_budget FROM budget where user_id = ? and category = ? and month = ? ''', 
                        (self.user_id, self.month, self.category,)
                        )
        budget = cursor.fetchone()[0]
        print(budget)
        if budget:
            print(f"Budget set for {self.category} for {self.month} is {self.monthly_budget[0]}")
        else:
            pass
        conn.close()


    def notify_users(self):
        conn = sqlite3.connect('finance.db')
        cursor = conn.cursor()
        cursor.execute('''
                        SELECT t.user_id , b.monthly_budget, sum(t.amount) as total_expense,
                        CASE 
                        WHEN sum(t.amount) > b.monthly_budget THEN "Limit Amount Exceeded"
                        ELSE "Within Budegt"
                        END AS budget_status
                        FROM Transactions as t join budget as b 
                        on t.user_id = b.user_id
                        WHERE t.category = 'expense' and substr(date ,1,7) = b.month
                        GROUP BY t.user_id, b.monthly_budget
                       ''')
        budget = cursor.fetchall()
        conn.close()