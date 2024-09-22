import shutil
import os

class DatabaseManager:
    def __init__(self, db_path='finance_management.db'):
        self.db_path = db_path

    def backup_database(self, backup_path='backup_finance_management.db'):
        """Backup the current database to the specified path."""
        try:
            shutil.copy(self.db_path, backup_path)
            print(f"Backup successful to {backup_path}")
        except FileNotFoundError:
            print(f"Source database file '{self.db_path}' does not exist.")
        except PermissionError:
            print(f"Permission denied when trying to access '{self.db_path}' or '{backup_path}'.")
        except Exception as e:
            print(f"Error during backup: {e}")

    def restore_database(self, backup_path='backup_finance_management.db'):
        """Restore the database from the specified backup path."""
        if not os.path.exists(backup_path):
            print(f"Backup file '{backup_path}' does not exist.")
            return

        confirmation = input(f"Are you sure you want to restore from '{backup_path}' to '{self.db_path}'? (yes/no): ")
        if confirmation.lower() != 'yes':
            print("Restore operation canceled.")
            return

        try:
            if os.path.exists(self.db_path):
                os.remove(self.db_path)
            shutil.copy(backup_path, self.db_path)
            print("Database restored successfully.")
        except PermissionError:
            print(f"Permission denied when trying to access '{backup_path}' or '{self.db_path}'.")
        except Exception as e:
            print(f"Error during restore: {e}")

# Example usage
if __name__ == "__main__":
    db_manager = DatabaseManager()
    db_manager.backup_database()
    db_manager.restore_database()
