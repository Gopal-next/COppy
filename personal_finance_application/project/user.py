import sqlite3

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
        self.password = password


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
        conn = sqlite3.connect('finance.db')
        cusror = conn.cursor()

        print(f"Your Password : {self.password}")
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
    
    
        
    def login(username):
        conn = sqlite3.connect('finance.db')
        cursor = conn.cursor()

        cursor.execute('SELECT id, username, password FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()  # Fetch the entire row

        if user is None:
            conn.close()
            raise ValueError("Username does not exist")

        conn.close()
        return {'id': user[0], 'username': user[1], 'password': user[2]}  # Return user as a dictionary

    #         # print("Login successful!")
    # def login(self):
    #     conn = sqlite3.connect('finance.db')
    #     cursor = conn.cursor()
    #     cursor.execute('SELECT password FROM users WHERE username=?', (self.username,))
    #     result = cursor.fetchone()
    #     conn.close()
    #     if result and result[0] == self.password:
    #         return True
    #     else:
    #         return False