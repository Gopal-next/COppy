# import click
# from project.app import FinanceApp


# app = FinanceApp()

# @click.command()
# @click.option('--username', prompt='Username', help='Your username')
# @click.option('--password', prompt='Password', help='Your password') #hide_input=True, confirmation_prompt=True, 
# def register(username, password):
#     """Register a new user"""
#     try:
#         app.register_user(username, password)
#         click.echo('User registered successfully!')
#     except ValueError as e:
#         click.echo(str(e))

# @click.command()
# @click.option('--username', prompt='Username', help='Your username')
# @click.option('--password', prompt='Password', help='Your password') #  hide_input=True,
# def login(username, password):
#     """Login as an existing user"""
#     try:
#         app.login_user(username, password)
#         click.echo('Login successful!')
#     except ValueError as e:
#         click.echo(str(e))
        
# @click.command()
# @click.option('--user_id',prompt = 'User Id',type = int , help = 'The ID of user for addinf transaction')
# @click.option('--transaction_type', prompt= 'Transaction Type', type = click.Choice(['income', 'expense']), help= 'The Type of Transaction')
# @click.option('--category', prompt='Category', help='From where you got the money or expend it like  food, rent , dress and so on...')
# @click.option('--amount',prompt= 'Amount', type= float, help = 'Type what amount u gain in income or spend in expense')
# # @click.option('--date', prompt="Enter Date (optional)", default = None,help='Enter the todays date')
# def add(user_id,transaction_type,category,amount):
#     ''' Add transaction as income or expense'''
#     try:
#         app.add_records(user_id,transaction_type,category,amount)
#         click.echo("Transaction added successfully")
#     except ValueError:
#         click.echo("efewf")


# @click.command()
# @click.option('--user_id',prompt = 'User Id',type = int , help = 'The ID of user for addinf transaction')
# def view(user_id):
#     ''' For viewing all Transaction'''
#     try:
#         app.all_transaction(user_id)
#         click.echo("All transaction")
#     except ValueError as e:
#         click.echo(e)

# @click.command()
# @click.option('--transaction_id', prompt= 'Transaction id', help='Type the transaction id you want to update')
# @click.option('--category',prompt='Category', help='Type the category')
# @click.option('--amount',prompt='Amount', help= 'Type the amount if its changed')
# # @click.option('--date', prompt='Date', help= 'Enter the Date')
# def update(transaction_id, category, amount):
#     ''' Update the Transaction'''
#     app.update_records(transaction_id, category, amount)
#     click.echo("Records updated successfully")

# @click.command()
# @click.option('--transaction_id', prompt='Transaction Id', help='Type the transaction id You want to delete')
# def delete(transaction_id):
#     ''' Delte the Transaction'''
#     app.delete_records(transaction_id)
#     click.echo("Records deleted successfully")

# @click.command()
# @click.option('--user_id',prompt = 'User Id',type = int , help = 'The ID of user for addinf transaction')
# @click.option('--month', prompt = 'Month', help = 'Enter the month in YYYY-MM format')

# def month_report(user_id,month):
#     ''' To view the monthly report'''
#     click.echo("Monthly report \n")
#     app.monthly_review(user_id,month)
    


# @click.command()
# @click.option('--user_id',prompt = 'User Id',type = int , help = 'The ID of user for addinf transaction')
# @click.option('--year', prompt = 'Year', help = 'Enter the month in YYYY-MM format')
# def YearlyReport(user_id,year):
#     ''' To view the yearly report'''
#     click.echo("Yearly report ")
#     app.yearly_review(user_id,year)
#     # click.echo("Yearly report")
    
# @click.command()
# @click.option('--user_id',prompt = 'User ID', help= 'Type the user id from which you want')
# @click.option('--type',prompt = 'type',type = click.Choice(['income', 'expense']) ,help= 'Fetch by category')

# def fetch(user_id,type):
#     ''' View all records by category'''
#     click.echo("All records")
#     app.fetch_category(user_id,type)

# @click.command()
# @click.option('--user_id',prompt = 'User ID', help= 'Type the user id from which you want')
# @click.option('--month',prompt = 'Month (Type as YYYY-MM)', help= 'Type the month from which you want')
# @click.option('--category',prompt='Category', help='Type the category')
# @click.option('--monthly_budget',prompt = 'Monthly Budget', help= 'Enter the Monthly budget that you want to set')
# def setbudget(user_id, month, category, monthly_budget):
#     ''' Set Budegt '''
#     # click.echo("Budegt set for given month")
#     try:
#         app.budget_set(user_id, month, category, monthly_budget)
#         click.echo("Budegt set for given month")
#     except ValueError as e:
#         click.echo(e)


# @click.command()
# @click.option('--user_id',prompt = 'User ID', help= 'Type the user id from which you want')
# @click.option('--month',prompt = 'Month (Type as YYYY-MM)', help= 'Type the month from which you want')
# @click.option('--category',prompt='Category', help='Type the category')
# # @click.option('--monthly_budget',prompt = 'Monthly Budget', help= 'Enter the Monthly budget that you want to set')
# def seebudget(user_id, month, category, monthly_budget):
#     ''' Set Budegt '''
#     click.echo("Budegt for given month")
#     app.budget_check(user_id, month, category)


# # user_id, month, category,monthly_budget
# @click.group()
# def cli():
#     """Personal Finance Management Application"""
#     pass

# cli.add_command(register)
# cli.add_command(login)
# cli.add_command(add)
# cli.add_command(view)
# cli.add_command(update)
# cli.add_command(delete)
# cli.add_command(month_report)
# cli.add_command(YearlyReport)
# cli.add_command(fetch)
# cli.add_command(setbudget)
# cli.add_command(seebudget)

# if __name__ == '__main__':
#     cli()


# # Username: ASDFG
# # Password:
# # Repeat for confirmation:
# # Hashed Password (for verification): Aa12!





import click
from project.app import FinanceApp

app = FinanceApp()

@click.command()
@click.option('--username', prompt='Username', help='Your username')
@click.option('--password', prompt='Password', help='Your password') #hide_input=True, confirmation_prompt=True, 
def register(username, password):
    """Register a new user"""
    try:
        app.register_user(username, password)
        click.echo('User registered successfully!')
    except ValueError as e:
        click.echo(str(e))

@click.command()
@click.option('--username', prompt='Username', help='Your username')
@click.option('--password', prompt='Password', help='Your password') 
def login(username, password):
    """Login as an existing user"""
    try:
        user_id = app.login_user(username, password)  # Get user ID from the login function
        click.echo('Login successful!')
        show_menu(user_id)  # Pass the user ID to show_menu
    except ValueError as e:
        click.echo(str(e))

@click.command()
def view(user_id):
    ''' For viewing all Transactions '''
    try:
        app.all_transaction(user_id)
        click.echo("All transactions listed successfully.")
    except ValueError as e:
        click.echo(str(e))

@click.command()
def add_transaction(user_id):
    ''' Add a transaction '''
    transaction_type = click.prompt('Transaction Type (income/expense)', type=click.Choice(['income', 'expense']))
    category = click.prompt('Category (e.g., food, rent)')
    amount = click.prompt('Amount', type=float)
    try:
        app.add_records(user_id, transaction_type, category, amount)
        click.echo("Transaction added successfully.")
    except ValueError as e:
        click.echo(str(e))

@click.command()
def update_transaction():
    ''' Update the Transaction '''
    transaction_id = click.prompt('Transaction Id', type=int)
    category = click.prompt('New Category')
    amount = click.prompt('New Amount', type=float)
    try:
        app.update_records(transaction_id, category, amount)
        click.echo("Transaction updated successfully.")
    except ValueError as e:
        click.echo(str(e))

@click.command()
def delete_transaction():
    ''' Delete the Transaction '''
    transaction_id = click.prompt('Transaction Id', type=int)
    try:
        app.delete_records(transaction_id)
        click.echo("Transaction deleted successfully.")
    except ValueError as e:
        click.echo(str(e))

@click.command()
def month_report(user_id):
    ''' Monthly report '''
    month = click.prompt('Enter the month (YYYY-MM)', type=str)
    try:
        app.monthly_review(user_id, month)
        click.echo("Monthly report generated.")
    except ValueError as e:
        click.echo(str(e))

@click.command()
def yearly_report(user_id):
    ''' Yearly report '''
    year = click.prompt('Enter the year (YYYY)', type=str)
    try:
        app.yearly_review(user_id, year)
        click.echo("Yearly report generated.")
    except ValueError as e:
        click.echo(str(e))

@click.command()
def set_budget(user_id):
    ''' Set Monthly Budget '''
    month = click.prompt('Month (YYYY-MM)', type=str)
    category = click.prompt('Category')
    monthly_budget = click.prompt('Monthly Budget', type=float)
    try:
        app.budget_set(user_id, month, category, monthly_budget)
        click.echo("Budget set successfully.")
    except ValueError as e:
        click.echo(str(e))

@click.command()
def check_budget(user_id):
    ''' Check Monthly Budget '''
    month = click.prompt('Month (YYYY-MM)', type=str)
    category = click.prompt('Category')
    try:
        app.budget_check(user_id, month, category)
        click.echo("Budget check complete.")
    except ValueError as e:
        click.echo(str(e))


# Function to show options after login
def show_menu(user_id):
    while True:
        click.echo("\nChoose an action:")
        click.echo("1. View all transactions")
        click.echo("2. Add a transaction")
        click.echo("3. Update a transaction")
        click.echo("4. Delete a transaction")
        click.echo("5. Monthly report")
        click.echo("6. Yearly report")
        click.echo("7. Set budget")
        click.echo("8. Check budget")
        click.echo("9. Exit")

        choice = click.prompt("Enter your choice", type=int)

        if choice == '1':
            view(user_id)
        elif choice == '2':
            add_transaction(user_id)
        elif choice == '3':
            update_transaction()
        elif choice == 4:
            delete_transaction()
        elif choice == 5:
            month_report(user_id)
        elif choice == 6:
            yearly_report(user_id)
        elif choice == 7:
            set_budget(user_id)
        elif choice == 8:
            check_budget(user_id)
        elif choice == 9:
            click.echo("Exiting...")
            break
        else:
            click.echo("Invalid choice. Please try again.")


@click.group()
def cli():
    """Personal Finance Management Application"""
    pass

cli.add_command(register)
cli.add_command(login)

if __name__ == '__main__':
    cli()
