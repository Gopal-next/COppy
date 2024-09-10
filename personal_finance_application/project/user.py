import sqlite3
from project.database import Database

class User:
    def __init__(self, username, password,db_name='finance.db'):
        if not (5 <= len(password) <= 16):
            raise ValueError("Password must be between 5 to 16 characters")
        if not any(char.islower() for char in password) or \
        not any(char.isupper() for char in password) or \
        not any(char.isdigit() for char in password) or \
        not any(char in '!@#$%^&*()' for char in password):
            raise ValueError("Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character")

        self.username = username
        # self.password = hashlib.sha256(password.encode()).hexdigest()
        self.password = password
        self.db = Database()
    
    def connect(self):
        return sqlite3.connect(self.db_name)

    @staticmethod
    def create_user_table():
        conn = sqlite3.connect('finance.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT NOT NULL UNIQUE,
                            password TEXT NOT NULL
                          )''')
        conn.commit()
        conn.close()

    def register(self):
        # self.db.create_user_table()
        conn = sqlite3.connect('finance_db')
        cusror = conn.cursor()
        # cusror.execute('SELECT username from users WHERE username = ?', (self.username,))
        # if cusror.fetchone():
        #     conn.close()
        #     raise ValueError("Username Already exists.")

        print(f"Hashed Password (for verification): {self.password}")
        # hashed_password = hashlib.sha256(self.password.encode()).hexdigest()
        # print(f"Hashed password during registration: {hashed_password}")
        
        try:
            cusror.execute(
                'INSERT INTO users (username, password) VALUES (?, ?)', (self.username, self.password)
            )
            conn.commit()
        except sqlite3.IntegrityError:
            raise ValueError("UserName Already exists")
        finally:
            conn.close()
        
    def login(self):
        conn = sqlite3.connect('finance_db')
        cursor = conn.cursor()

        # Retrieve the stored hashed password for the provided username
        cursor.execute('SELECT password FROM users WHERE username = ?', (self.username,))
        stored_password = cursor.fetchone()

        if stored_password is None:
            conn.close()
            print("Username does not exist")    
        
        
        print(f"Stored hashed password from database: {stored_password[0]}")

        # Verify the provided password with the stored hashed password

        # hashed_input_password = hashlib.sha256(self.password.encode()).hexdigest()
        # print(f"Hashed input password during login: {hashed_input_password}")
        if self.password != stored_password[0]:
            conn.close()
            raise ValueError("Incorrect password")

        conn.close()
        # print("Login successful!")
