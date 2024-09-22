
# # Username: ASDFG
# # Password:
# # Repeat for confirmation:
# # Hashed Password (for verification): Aa12!

import click
import click.core
from project.app import FinanceApp
from click import get_current_context
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
        app.monthly_review(user_id,month)
        click.echo("Monthly report generated.")
    except ValueError as e:
        click.echo(str(e))

@click.command()
def yearly_report(user_id):
    ''' Yearly report '''
    year = click.prompt('Enter the year (YYYY)', type=str)
    try:
        app.yearly_review( user_id,year)
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
def view_all_budget(user_id):
    ''' See Your Budeget'''
    try:
        app.see_all_budegt(user_id)
        click.echo("All Budget listed successfully.")
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
        click.echo("8. View Budget")
        click.echo("9. Exit")

        choice = click.prompt("Enter your choice", type=int)
        ctx = get_current_context()

        if choice == 1:
            ctx.invoke(view, user_id=user_id)
        elif choice == 2:
            ctx.invoke(add_transaction, user_id=user_id)
        elif choice == 3:
            ctx.invoke(update_transaction)  # Fix: Use ctx.invoke for update_transaction
        elif choice == 4:
            ctx.invoke(delete_transaction)  # Fix: Use ctx.invoke for delete_transaction
        elif choice == 5:
            ctx.invoke(month_report, user_id=user_id)
        elif choice == 6:
            ctx.invoke(yearly_report, user_id=user_id)
        elif choice == 7:
            ctx.invoke(set_budget, user_id=user_id)
        elif choice == 8:
            ctx.invoke(view_all_budget, user_id=user_id)
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

